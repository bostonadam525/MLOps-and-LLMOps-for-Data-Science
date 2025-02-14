## Step 1: Create the main processing script
## Run this in a notebook cell:

%%writefile process_skills_behaviors.py

import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import asyncio
from tqdm.notebook import tqdm
import os
import argparse

class SkillBehaviorProcessor:
    def __init__(self, model_name="google/gemma-2-9b-it", offload_folder="/tmp/offload"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Quantization configuration
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
        )
        
        # Load model with offloading
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            quantization_config=bnb_config,
            device_map="auto",
            torch_dtype=torch.bfloat16,
            offload_folder=offload_folder
        )

        # Enable gradient checkpointing
        self.model.gradient_checkpointing_enable()

    def generate_text(self, prompt, max_new_tokens=256):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(**inputs, max_new_tokens=max_new_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    async def generate_pseudo_label_async(self, text):
        prompt = f"""<start_of_turn>user
Given the following text, identify and extract key phrases related to work behaviors, hard skills, and soft skills demonstrated. Use a step-by-step approach:

Text: "{text}"

Step 1: Identify potential work behaviors, hard skills, and soft skills mentioned in the text.
Step 2: For each identified item, determine if it's a work behavior, hard skill, or soft skill.
Step 3: Formulate concise phrases for each work behavior, hard skill, and soft skill.
Step 4: List the work behaviors, hard skills, and soft skills separately.

Output the results in the following format:
Work Behaviors:
1. [Work Behavior phrase]
2. [Work Behavior phrase]
3. [Work Behavior phrase]

Hard Skills:
1. [Hard Skill phrase]
2. [Hard Skill phrase]
3. [Hard Skill phrase]

Soft Skills:
1. [Soft Skill phrase]
2. [Soft Skill phrase]
3. [Soft Skill phrase]

If fewer than three are evident for any category, list only those that are clearly demonstrated.
If there are no hard or soft skills found just say "No skills". 
If there are no work behaviors found just say "No behaviors". 
If there are neither skills nor behaviors found in the text just say "None". 
<end_of_turn>
<start_of_turn>model
"""
        return self.generate_text(prompt)

    async def classify_behaviors_and_skills_async(self, behaviors, hard_skills, soft_skills):
        prompt = f"""<start_of_turn>user
Given the following work behaviors, hard skills, and soft skills, classify them into general categories:

Work Behaviors: {behaviors}
Hard Skills: {hard_skills}
Soft Skills: {soft_skills}

Provide a general classification for the behaviors, hard skills, and soft skills. Output the results in the following format:
Behavior Class: [General category for behaviors]
Hard Skill Class: [General category for hard skills]
Soft Skill Class: [General category for soft skills]

If there are no hard or soft skills found just classify it as "No skills". 
If there are no work behaviors found just classify it as "No behaviors". 
If there are neither skills nor behaviors found in the text just say "None". 
<end_of_turn>
<start_of_turn>model
"""
        return self.generate_text(prompt)

    async def process_extraction_batch_async(self, batch):
        return [await self.generate_pseudo_label_async(text) for text in batch]

    async def process_classification_batch_async(self, batch):
        return [await self.classify_behaviors_and_skills_async(row['work_behaviors'], row['hard_skills'], row['soft_skills']) for _, row in batch.iterrows()]

    async def process_extraction_dataframe_async(self, series, batch_size=10):
        results = []
        total_batches = (len(series) + batch_size - 1) // batch_size
        for i in tqdm(range(0, len(series), batch_size), total=total_batches, desc="Processing extraction batches"):
            batch = series.iloc[i:i+batch_size]
            batch_results = await self.process_extraction_batch_async(batch)
            results.extend(batch_results)
        return results

    async def process_classification_dataframe_async(self, df, chunk_size=100):
        results = []
        total_chunks = (len(df) + chunk_size - 1) // chunk_size
        for i in tqdm(range(0, len(df), chunk_size), total=total_chunks, desc="Processing classification chunks"):
            chunk = df.iloc[i:i+chunk_size]
            batch_results = await self.process_classification_batch_async(chunk)
            results.extend(batch_results)
        return results

    @staticmethod
    def extract_skills_and_behaviors(text):
        work_behaviors, hard_skills, soft_skills = [], [], []
        current_category = None
        for line in text.split('\n'):
            if line.startswith('Work Behaviors:'):
                current_category = 'behaviors'
            elif line.startswith('Hard Skills:'):
                current_category = 'hard_skills'
            elif line.startswith('Soft Skills:'):
                current_category = 'soft_skills'
            elif line.strip().startswith(('1.', '2.', '3.')):
                item = line.split('.', 1)[1].strip()
                if current_category == 'behaviors':
                    work_behaviors.append(item)
                elif current_category == 'hard_skills':
                    hard_skills.append(item)
                elif current_category == 'soft_skills':
                    soft_skills.append(item)
        return ', '.join(work_behaviors), ', '.join(hard_skills), ', '.join(soft_skills)

    @staticmethod
    def extract_classifications(classifications):
        behavior_class = hard_skill_class = soft_skill_class = ''
        for line in classifications.split('\n'):
            if line.startswith('Behavior Class:'):
                behavior_class = line.split(':', 1)[1].strip()
            elif line.startswith('Hard Skill Class:'):
                hard_skill_class = line.split(':', 1)[1].strip()
            elif line.startswith('Soft Skill Class:'):
                soft_skill_class = line.split(':', 1)[1].strip()
        return behavior_class, hard_skill_class, soft_skill_class

    def run_async(self, coro):
        return asyncio.get_event_loop().run_until_complete(coro)

    def process_dataframe(self, df, extraction_batch_size=32, classification_chunk_size=128, save_interval=10000, output_dir='/opt/ml/processing/output'):
        print(f"Processing dataframe with {len(df)} rows")
        
        result_df = df.copy()
        
        print("Extracting skills and behaviors...")
        pseudo_labels = self.run_async(self.process_extraction_dataframe_async(result_df['english_message'], extraction_batch_size))
        result_df['pseudo_labels'] = pseudo_labels
        result_df['work_behaviors'], result_df['hard_skills'], result_df['soft_skills'] = zip(*result_df['pseudo_labels'].apply(self.extract_skills_and_behaviors))
        
        print("Classifying behaviors and skills...")
        temp_df = result_df[['work_behaviors', 'hard_skills', 'soft_skills']].copy()
        classifications = self.run_async(self.process_classification_dataframe_async(temp_df, classification_chunk_size))
        result_df['classifications'] = classifications
        result_df['behavior_class'], result_df['hard_skill_class'], result_df['soft_skill_class'] = zip(*result_df['classifications'].apply(self.extract_classifications))
        
        # Periodic saving
        os.makedirs(output_dir, exist_ok=True)
        for i in range(0, len(result_df), save_interval):
            chunk = result_df.iloc[i:i+save_interval]
            chunk.to_csv(f'{output_dir}/results_chunk_{i//save_interval}.csv', index=False)
            print(f"Saved chunk {i//save_interval}")
        
        print(f"Processed {len(result_df)} rows")
        print(f"Sample results:\n{result_df[['english_message', 'work_behaviors', 'hard_skills', 'soft_skills', 'behavior_class', 'hard_skill_class', 'soft_skill_class']].head()}")
        
        return result_df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-data-dir', type=str, default='/opt/ml/processing/input')
    parser.add_argument('--output-data-dir', type=str, default='/opt/ml/processing/output')
    args, _ = parser.parse_known_args()
    
    # Initialize the processor
    processor = SkillBehaviorProcessor(offload_folder='/tmp/offload')
    
    # Load your data
    input_files = [f for f in os.listdir(args.input_data_dir) if f.endswith('.csv')]
    if not input_files:
        raise ValueError(f"No CSV files found in {args.input_data_dir}")
    
    input_file = os.path.join(args.input_data_dir, input_files[0])
    df_qlik = pd.read_csv(input_file)
    
    # Process the DataFrame
    result_df = processor.process_dataframe(
        df_qlik,
        extraction_batch_size=32,
        classification_chunk_size=128,
        save_interval=10000,
        output_dir=args.output_data_dir
    )
    
    # Save the final results
    result_df.to_csv(os.path.join(args.output_data_dir, 'final_results.csv'), index=False)
    print("Processing complete. Results saved.")

## -----------------------------------------------------------------------------------------------------
## Step 2: Upload the processing script to S3
## Run this in a new notebook cell:

import boto3

s3 = boto3.resource('s3')
bucket_name = <'your bucket name'>
object_key = <'file_location/file_name.py'>

with open('process_skills_behaviors.py', 'rb') as file:
    s3.Object(bucket_name, object_key).put(Body=file)

print(f"File uploaded to s3://{bucket_name}/{object_key}")

## -----------------------------------------------------------------------------------------------------
## Step 3: Create the SageMaker Processing job configuration
## Run this in a new notebook cell:
%%writefile sagemaker_processing_job.py

from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker.pytorch.processing import PyTorchProcessor

role_arn = '<your arn goes here>'  # Your actual role ARN

pytorch_processor = PyTorchProcessor(
    framework_version='1.10',
    role=role_arn,
    instance_type='ml.g5.2xlarge', ## GPU instance you are using
    instance_count=1,
    base_job_name='<name of job>',
    py_version='py38'
)

pytorch_processor.run(
    code='s3://<your bucket name>/file_location/file_name.py',
    inputs=[
        ProcessingInput(
            source='s3://<your bucket name>/file_location/inputs',
            destination='/opt/ml/processing/input'
        )
    ],
    outputs=[
        ProcessingOutput(
            output_name='<name_of_output>',
            source='/opt/ml/processing/output',
            destination='s3://<your bucket name/file_location/outputs'
        )
    ],
    arguments=['--input-data-dir', '/opt/ml/processing/input',
               '--output-data-dir', '/opt/ml/processing/output']
)

## -----------------------------------------------------------------------------------------------------
## Step 4: Run the SageMaker Processing job
## Run this in a new notebook cell:
%run sagemaker_processing_job.py

## This script allows you to utilize the Amazon Translate API 
## 1. First thing you need to do is make sure your IAM role is updated to allow access to this service. 
# If you are going to use this service you have to update your Sagemaker studio IAM role policy:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "translate:TranslateText",
                "translate:GetTerminology",
                "translate:ListTerminologies",
                "comprehend:DetectDominantLanguage",
                "comprehend:BatchDetectDominantLanguage"
            ],
            "Resource": "*"
        }
    ]
}
### Code below is to use when NOT using translation accuracy metrics
import boto3
import pandas as pd

# Set up the AWS Translate client
translate = boto3.client('translate', region_name='your-region')

def translate_text(text, source_lang='auto', target_lang='en'):
    try:
         response = translate.translate_text(
             Text=text,
             SourceLanguageCode=source_lang,
             TargetLanguageCode=target_lang
         )
         return response['TranslatedText']
     except Exception as e:
         print(f"Error translating text: {e}")
         return text  # Return original text if translation fails

## Load your DataFrame
 df = pd.read_csv('your_data.csv')  

## Apply translation to a specific column
df['translated_column'] = df['text_column'].apply(translate_text)

## Save the updated DataFrame if needed
df.to_csv('translated_data.csv', index=False)


### Code below allows you to use built-in translation accuracy metrics from AWS Translation service.
## Note: If you are using the "auto" setting to have the API detect the language prior to translating then the 
## accuracy metrics may not work as the detected language is not considered a "ground truth". 
## to use the built-in accuracy metrics do the language detection first
import boto3
import pandas as pd
from tqdm import tqdm

# Set up the AWS Translate client
translate = boto3.client('translate', region_name='<your region here>')

## translate text function -- change `source_lang` based on your data
def translate_text(text, source_lang='auto', target_lang='en'):
    try:
        response = translate.translate_text(
            Text=text,
            SourceLanguageCode=source_lang,
            TargetLanguageCode=target_lang
        )
        return {
            'translated_text': response['TranslatedText'],
            'source_language': response['SourceLanguageCode'],
            'confidence_score': response.get('TranslationConfidence', {}).get('Score')
        }
    except Exception as e:
        print(f"Error translating text: {e}")
        return {'translated_text': text, 'source_language': None, 'confidence_score': None}

# Apply translation to a specific column and expand the result with tqdm progress_bar
tqdm.pandas(desc="Translating")
df_translate[['translated_column', 'detected_source_language', 'confidence_score']] = df_translate['message'].progress_apply(translate_text).apply(pd.Series)

# Save the updated DataFrame if needed
df_translate.to_csv('translated_data_with_metrics.csv', index=False)




#### Filter and Merge Data
# If you need to merge your original dataframe lets say its called `df_final` with the translation dataframe you used lets say its called `df_translate`.
# The goal is to take the original message column of only the english messages from the df_final and the translated messages from the "translated_column" in df_translate.
## This script will help with this merge/join operation

# 1. First, merge df_translate back to df_final
# Make sure you're merging on the correct column(s) that link these DataFrames
df_merged = df_final.merge(df_translate[['message', 'translated_column']], on='message', how='left')

# 2. Now create the new column 'final_message_text'
df_merged['final_message_text'] = np.where(
    df_merged['language_label'] == 'en',
    df_merged['message'],  # If English, use original message
    df_merged['translated_column']  # If not English, use translated text
)

# 3. If you want to drop the intermediate columns:
df_merged = df_merged.drop(columns=['translated_column'])

# 4. If you want to rename df_merged back to df_final:
df_final = df_merged

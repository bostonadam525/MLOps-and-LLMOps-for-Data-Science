# Building with AWS Bedrock
* This repo contains the basic steps to build with AWS Bedrock. 

# Project Examples
* `app.py` -- this is #1 below
1. Document RAG PDF Document Question & Answer application.
    * PDF document --> embeddings (Amazon Titan embeddings) --> FAISS-CPU vector library
    * RAG-LLM pipeline with AWS Bedrock using `Claude-3-Haiku LLM` and `Llama-3`
        * User asks question --> similarity search in FAISS vector store
        * Relevant chunks retrieved --> sent to LLM with prompt--> Answer to query


# Important Setup Steps
1. Create a virtual environment using anaconda.
    * run this code: `conda create -p venv python==<version of python you want> -y`
    * or create venv: `python -m venv <name of venv>`

2. To activate the conda venv
    * run this code: `conda activate venv/`

3. Install requirements file
    * The only requirements for this project are:
        * `boto3`
        * `awscli`
    * run this code: `pip install -r aws_bedrock_requirements.txt`

4. Create IAM user
    * If you haven't already created IAM role.
    * Log into AWS console.
        * Go to `IAM`
        * If a user is not created then create one and `attache policies directly`.
    * Once you have the user information you can `create access key`.

5. To run AWS CLI
    * run this first: `aws configure`
    * Input `AWS Acess Key ID`
    * Input `AWS Secret Access Key`
    * AWS Region: default is `us-east-1` (press enter)
    * Choose default output format: `json`

6. Bedrock model access
    * May need to request model access based on region location.
    * Pick a model you have access to. 
    * Need to access the `API request` code.

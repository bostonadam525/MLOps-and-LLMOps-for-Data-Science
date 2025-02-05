## 1. Basic Script for loading files from S3 bucket in AWS to SageMaker
import boto3
import pandas as pd
from sagemaker import get_execution_role

# Create S3 client
conn = boto3.client('s3')

# S3 bucket name
bucket = '<name of your bucket>'

# Correct data_key (remove the leading slash)
data_key = '<folder_name/sub_folder_name/file_name.pkl>'

# Construct the full S3 URI
data_location = f's3://{bucket}/{data_key}'

# Load the DataFrame
try:
    df = pd.read_pickle(data_location)
    print(df.head())
except Exception as e:
    print(f"An error occurred: {e}")
    
    # List objects in the bucket to check if the file exists
    response = conn.list_objects_v2(Bucket=bucket, Prefix='company_health_experiment/results/')
    
    if 'Contents' in response:
        print("Files in the specified S3 location:")
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("No files found in the specified S3 location.")



## 2. Another S3 script to load data into AWS SageMaker

import boto3
from sagemaker import get_execution_role
conn = boto3.client('s3')

## load s3 bucket
bucket = '<name of your bucket>'
content = conn.list_objects(Bucket=bucket)['Contents']
data_key= '<folder_name/file_name.csv>'
data_location= 's3://{}/{}'.format(bucket,data_key)

## load df
df = pd.read_csv(data_location, index_col= False, low_memory=False)
df.head()

## 1. Basic Script for loading 1 file from S3 bucket in AWS to SageMaker
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
    response = conn.list_objects_v2(Bucket=bucket, Prefix='<name_of_your_folder/name_of_your_folder/')
    
    if 'Contents' in response:
        print("Files in the specified S3 location:")
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("No files found in the specified S3 location.")



## 2. Loading multiple files from S3 bucket in AWS 
import boto3
import pandas as pd
from sagemaker import get_execution_role

# Create S3 client
conn = boto3.client('s3')

# S3 bucket name
bucket = '<name of your bucket>'

# Folder path in the S3 bucket
folder_path = '<name_of_folder_path/>' ## make sure you have correct path if in multiple folders

# CSV file names
file1 = 'file_1.csv'
file2 = 'file_2.csv'  

# Construct the full S3 URIs
data_location1 = f's3://{bucket}/{folder_path}{file1}'
data_location2 = f's3://{bucket}/{folder_path}{file2}'

# Function to load CSV and handle errors
def load_csv_from_s3(data_location):
    try:
        df = pd.read_csv(data_location)
        print(f"Successfully loaded: {data_location}")
        return df
    except Exception as e:
        print(f"An error occurred while loading {data_location}: {e}")
        return None

# Load the DataFrames
df1 = load_csv_from_s3(data_location1)
df2 = load_csv_from_s3(data_location2)

# Print the heads of the DataFrames if they were successfully loaded
if df1 is not None:
    print("\nFirst 5 rows of df1:")
    print(df1.head())

if df2 is not None:
    print("\nFirst 5 rows of df2:")
    print(df2.head())

# If there were errors, list the contents of the folder
if df1 is None or df2 is None:
    print("\nListing contents of the S3 folder:")
    response = conn.list_objects_v2(Bucket=bucket, Prefix=folder_path)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("No files found in the specified S3 location.")





## 3. Another simple S3 script to load data into AWS SageMaker

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

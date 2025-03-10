## This file has python scripts that can be utilized for monitoring deployed models.
## The code may need to be refactored to work with your model/instance


### 1. CloudWatch Logs
import boto3

logs_client = boto3.client('logs')

log_group_name = f"/aws/sagemaker/Endpoints/<name of model>"

# Get the latest log stream
response = logs_client.describe_log_streams(
       logGroupName=log_group_name,
       orderBy='LastEventTime',
       descending=True,
       limit=1
   )

if response['logStreams']:
    log_stream_name = response['logStreams'][0]['logStreamName']
       
# Get the log events
response = logs_client.get_log_events(
           logGroupName=log_group_name,
           logStreamName=log_stream_name,
           limit=100  # Adjust as needed
       )
       
for event in response['events']:
    print(event['message'])



### 2. CloudWatch Metrics
## You can monitor endpoint metrics like invocations, latency, and errors via CloudWatch.
import boto3
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')

response = cloudwatch.get_metric_statistics(
       Namespace='AWS/SageMaker',
       MetricName='Invocations',
       Dimensions=[
           {'Name': 'EndpointName', 'Value': '<name of deployed model>'},
           {'Name': 'VariantName', 'Value': 'AllTraffic'}
       ],
       StartTime=datetime.utcnow() - timedelta(hours=1),
       EndTime=datetime.utcnow(),
       Period=300,
       Statistics=['Sum']
   )

for datapoint in response['Datapoints']:
    print(f"Time: {datapoint['Timestamp']}, Invocations: {datapoint['Sum']}")



### 3. Monitor GPU Utilization
import boto3

cloudwatch = boto3.client('cloudwatch')

response = cloudwatch.get_metric_statistics(
       Namespace='AWS/SageMaker',
       MetricName='GPUUtilization',
       Dimensions=[
           {'Name': 'EndpointName', 'Value': '<name of deployed model>'},
           {'Name': 'VariantName', 'Value': 'AllTraffic'}
       ],
       StartTime=datetime.utcnow() - timedelta(hours=1),
       EndTime=datetime.utcnow(),
       Period=300,
       Statistics=['Average']
   )

for datapoint in response['Datapoints']:
    print(f"Time: {datapoint['Timestamp']}, GPU Utilization: {datapoint['Average']}%")


### 4. Email Notifications with logs
### You can set up SNS notifications for when the process completes or if there are any errors.
import boto3

sns = boto3.client('sns')

topic_arn = 'your-sns-topic-arn'  # Create this in the SNS console

sns.publish(
       TopicArn=topic_arn,
       Subject='Processing Job Status',
       Message='Your SageMaker processing job has completed successfully!'
    )



### 4. View Outputs and Results in S3 bucket
import boto3
import pandas as pd

## boto client
s3 = boto3.client('s3')

bucket = '<name of your S3 bucket>'
key = '<name of deployed model>/outputs/processed_results.csv'

## load data from bucket
obj = s3.get_object(Bucket=bucket, Key=key)
df = pd.read_csv(obj['Body'])

## print outputs
print(df.head())
print(f"Total rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")



### 5. Delete Endpoint
## While this is not a monitoring method, it is important to always delete your endpoint when finished. 

# Delete the endpoint
predictor.delete_endpoint()
print("Endpoint deleted")

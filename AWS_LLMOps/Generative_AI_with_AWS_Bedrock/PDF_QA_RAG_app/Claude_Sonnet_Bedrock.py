import boto3
import json
import certifi

# Setup bedrock client
#bedrock = boto3.client(service_name='bedrock-runtime')
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='<your region here>',
    verify=certifi.where() ## to avoid SSL error
)

# Your prompt
prompt_text = "Act as Shakespeare and write a poem on Jazz Music."

# Payload
payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1000,
    "messages": [
        {
            "role": "user",
            "content": prompt_text
        }
    ]
}

# Convert payload to JSON string
body = json.dumps(payload)

# Model ID for Claude 3 Sonnet
model_id = "<model id here>"

# Invoke the model
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# # Parse and print the response -- Claude-Sonnet 
response_body = json.loads(response.get("body").read())
response_text = response_body['content'][0]['text']
print(response_text)


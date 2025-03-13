# AWS Lambda with AWS Bedrock App
* This is a project demonstrating how to use AWS Lambda compute service to leverage AWS Bedrock foundation models.



# Architecture
* This is a flow diagram of the application I created using excalidraw:

![image](https://github.com/user-attachments/assets/6f35e329-1151-4498-a8b6-9a1b3c8b3db6)



## AWS Lambda
* AWS Lambda is a serverless compute service, offering automatic scaling and pay-as-you-go pricing, while EC2 provides virtual servers with full control and flexibility, making Lambda better for **event-driven, short-running tasks** vs EC2 for long-running, resource-intensive applications.

### How to Create Lambda functions in AWS
1. Click “Create function” 
2. Select “author from scratch” vs. “use a blueprint” vs. “container image” depending on your use case
3. Give lambda function a name: adamBedrockDataSciTestApp
4. Choose runtime —> e.g. Python 3.12
5. Architecture —> defaults to `x_86_64`
6. Create Function


### When to Choose Lambda vs. EC2? 
1. **Choose Lambda if:**
  * You need a serverless solution for event-driven tasks. 
  * You want to minimize infrastructure management. 
  * You need automatic scaling. 
  * Cost is a major concern, especially for intermittent workloads. 

2. **Choose EC2 if:**
* You need full control over your infrastructure. 
* You have long-running applications or resource-intensive workloads. 
* You need to run specific operating systems or software. 
* You need more flexibility in terms of storage and networking. 

# AWS Bedrock Agents
* Bedrock agents allow you to utilize AWS Bedrock Foundation Models and APIs to break down user requests to send to the correct agentic workflow.
* There are various ways to utilize Bedrock Agents including:
  1. Multi-agent collaboration and workflows
  2. RAG - Retrieval Augmented Generation
  3. Knowledge Bases
  4. API orchestration
  5. Code interpretation
  6. Prompt Engineering
 

# Agents with Knowledge Bases
* You have the option of:
  1. **Action Groups** - these define the actions that the agent can help end users perform. Each action group includes the parameters that the agent must elicit from the end-user. You can also define the APIs that can be called, how to handle the action, and how to return the response. 
  2. **Knowledge bases**
  3. Action groups and Knowledge bases
* This is an example of how agents can break down complex tasks into subtasks.
* The agents are able to determine the correct sequence of events (e.g. tools, APIs, data sources) and execute the actions to integrate data and knowledge bases during retrieval to augment an LLM's synthesized output to the user.

![image](https://github.com/user-attachments/assets/37eda796-4984-4eeb-b8b5-c4d3aa87ba10)


# Agent Automation
* The great thing about the agent framework in Bedrock is that it can orchestrate and automate multiple actions within the Generative AI pipeline as seen in this diagram below.

![image](https://github.com/user-attachments/assets/d34caa89-02f5-4b18-9b1a-95aa1f0a04b0)


# Agentic Workflow with Knowledge Bases: Action Groups & Knowledge Bases

## Action Groups
* When you ask a question of an LLM based application, the Bedrock agent will trigger a Bedrock Action Group.
* Action Groups are usually defined by business logic.
    * As an example, if you are building an insurance application and want a user to create a "claim", then you would have a specific action group devoted to creating a claim.
    * As another example, lets say a user needs to upload their documents to process an insurance claim. Then you would create an action group to trigger this workflow.
 
### Action Group Workflow
* Taking the example of the "create an insurance claim" above, the workflow would look like this:
  1. User needs to create a claim.
  2. Agent triggers "Create Claim" action group.
  3. AWS Lambda function triggered -- lambda function has business logic stored. 
  4. Data stored in a database such as AWS DynamoDB.
 

![image](https://github.com/user-attachments/assets/bb935837-c8ce-4c60-9729-48619ca71f2d)

 
## Agentic Knowledge base workflow
* There are times when a user's query may not need an Action group but rather a search and retrieval from the document store in your knowledge base. 

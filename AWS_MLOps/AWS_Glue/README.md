# AWS Glue

---
# What is AWS Glue?
- Fully managed ETL platform
- Spark and Python ETL engine
- Central Metadata repository --> Glue data catalog
- Flexible scheduler (runs it for you)
- [AWS Glue Concepts](https://docs.aws.amazon.com/glue/latest/dg/components-key-concepts.html)


<img width="768" height="576" alt="image" src="https://github.com/user-attachments/assets/594d8740-ddf8-4b76-a29b-777aa90378ac" />

---
## AWS Cloudformation
- [CloudFormation docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- AWS CloudFormation is a managed service provided by Amazon Web Services that allows you to define, provision, and manage your cloud infrastructure using code.
- It falls under the category of Infrastructure as Code (IaC), meaning ***instead of manually clicking through the AWS Management Console to build servers, databases, and networks, you write down your desired setup in a configuration file.**
- CloudFormation operates on two primary concepts:


1. **Templates:** These are the blueprints for your infrastructure. Written in either YAML or JSON format, these text files declare exactly what AWS resources you need (such as Amazon EC2 instances, Amazon S3 buckets, or RDS databases) and how they should be configured. Because they are text files, you can manage them in version control systems like Git just like regular software code

2. **Stacks:** When you upload a template into CloudFormation, the service generates a "stack". A stack is a single, unified group of AWS resources. If you delete the stack, CloudFormation automatically cleans up and deletes all the underlying resources associated with it, preventing leftover components from driving up costs

---
### Why should you use CloudFormation?
1. **Automation & Repeatability:** You can use a single template to spin up identical production, staging, and development environments across multiple AWS regions or accounts seamlessly.

2. **Dependency Management:** CloudFormation is smart enough to understand resource dependencies. For example, if an EC2 instance needs to live inside a specific security group, CloudFormation will build the security group first, wait for it to be ready, and then build the instance.

3. **Safety & Rollbacks:** If something goes wrong during a stack update or deployment, CloudFormation automatically executes a rollback, reverting your infrastructure back to its last known stable state.


4. **Change Sets:** Before applying updates to a live environment, you can generate a Change Set. This acts as a preview, showing you exactly which resources will be added, modified, or destroyed before you hit "execute"


5. **Drift Detection:** It monitors your environment to identify if anyone has manually tampered with or modified your AWS resources outside of the CloudFormation template

---
### How to use AWS CloudFormation
- Go to CloudFormation in the console.
- Click on "Create Stack"
- Choose Template type: **Existing template** or **Template Studio**
- Specify Template type: S3, Upload or Sync from Git
- Name your stack
- Name S3 bucket --> in AWS each bucket needs to be globally unique
- Create stack
- Make sure S3 bucket exists via "Outputs" column.
- CloudFormation creates IAM role automatically for you given the YAML file input.
  - Go to IAM --> Roles --> Policy attached

### Data access in S3
- S3 bucket needs data so go to S3 --> Create folders for data:
  - Name folder (e.g. rawData)
  - Create Folder
- Upload data to `rawData` folder or other data folders.

---
# AWS Glue Data Catalog
- **Purpose: Persistent Metadata Store for ANY data you have stored in any data source in AWS**
- **Examples of Metadata you can store:**
  - Data location
  - Schema
  - Data types
  - Data classification
- **What it does:**
  - Managed service that lets you store, annotate, and share metadata which can be used to query and transform your data.
  - **Lets you perform ETL on any data type using this persistent metadata store.***
  - **DOES NOT STORE ACTUAL DATA, ONLY METADATA OR REFERENCE INFORMATION required to get to the data that you have stored in AWS.**
  - There is ONE AWS Glue Data Catalog per AWS region.
  - IAM policies role access control.
  - Data governance

---
# AWS Glue Databases
- Set of associated Glue Data Catalog table definitions organized into logical groups.

---
# How AWS Glue Supports RAG and Agents
- **Central Lineage Registry:** Register your knowledge base source documents as tables in the AWS Glue Data Catalog using automatic crawlers to track data provenance, extraction methods, and audit trails
- **Metadata Filtering:** Combine structured metadata from Glue with vector embeddings (stored in Amazon OpenSearch or Aurora) so your RAG agents retrieve operationally correct context rather than just matching text similarity.
- **Automated Enrichment:** Use foundation models via Amazon Bedrock to generate clean JSON table and column descriptions automatically, updating your Glue catalog via API to improve agent discoverability.
- **Auditing via Athena:** Query your retrieval logs and data lineage seamlessly using Amazon Athena joined against your Glue metadata tables without writing custom application code

---
# How to Create Database in AWS Glue
- Go to Data Catalog --> Databases
- Name Database
- Use location link (e.g. S3 URI link)
- Create Database (done)

---
# AWS Glue Tables
- Metadata definition that represents your data!
- Data resides in its original store.
- **Representation of data schema -- thats it, its not the actual data itself.**

## Creating Glue Tables -- Manual
- Go to Tables on side bar under **Data Catalog --> Databases**
- **Add Table**
- Name table(s)
- Choose table format: Standard vs. Apache Iceberg
- Select Datastore: S3, kinesis, kafka
- account --> if choosing "my account" need S3 URI
- Select data type (e.g. CSV, JSON)
- Customize schema and dtypes

## Creating Glue Tables -- Crawlers
- Left hand menu select
- **Create Crawler**
- Name crawler
- Add data source --> S3 URI link
- Crawl all sub-folders
- Add S3 source
- Select IAM role
- Select Target Database
- Select Crawler Schedule (e.g. on-demand, hourly, etc.)
- Create Crawler
- **Run Crawler**
- **Check Tables to make sure it populated and is correct schemas**

---
# Partitions in AWS
- Folders where data is stored in S3 which are physical entities mapped to partitions which are logical entities
- e.g. Columns in a Glue Table
- **Important way to speed up queries**

---
# AWS Glue Connetions
- Data Catalog object that contains properties that are required to connect to a specific data store in AWS.
- Easily accessible on sidebar.

---
# AWS Glue ETL 
- Supports data extraction from numerous sources.
- Transforms data to your specific business requirements.
- Loads into destination of choice.

---
## Visual ETL in Glue
- This is a good way to map out your ETL process. Under the hood it will create a code script if you want to modify or use it in the future.
- **Visual ETL process:**
  - Name job
  - Edit Job details --> IAM role (make sure populates)
  - Advanced config
    - Browse for Script location for S3
    - Browse for Script Path for S3 --> add `/logs/`
    - Browse for Temporary Path --> TempDir
    - Set **Requested number of workers** --> 2 to 10 or whichever matches your data
  - Save job
 
### 1. Add ETL nodes

<img width="1163" height="488" alt="Screenshot 2026-10-03 094756" src="https://github.com/user-attachments/assets/165ec66b-8375-439a-853a-172fdb29bd31" />


### 2. Add Transform
- Add current timestamp


### 3. Add Target
- File type: Parquet
- Compression type: Snappy
- S3 process location: processed data folder in your S3 bucket --> add tag to name target
- Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions
- Select Database
- Name Database table
- Add partition key (e.g. timestamp transformation)

### 4. Save job
- save your ETL job!


---
# AWS Glue ETL Engine
- Apache Spark engine to distribute BIG DATA workloads across worker nodes (similar to Databricks)
- Also supports Python, but SPARK is preferred.

---
# AWS Glue DPUs
- 1 DPU is equal to 4 vCPUs and 16 GB of memory.
- Rules of thumb:
  - Not enough DPUs and system will crash.
  - Too many DPUs and cost will skyrocket.
- Use console to monitor provisions of DPUs.

---
# AWS Glue Bookmarks
- This tracks data that has already been processed during previous runs of ETL jobs by persisting state information from job run.
- When new data arrives --> can process new data without disrupting previous data. 
  

---
# AWS Glue Crawlers
- Connects to a data store (e.g. source or target)
- Progresses through prioritized list of classifiers to **determine schema of your data --> Creates metadata tables in AWS Glue Data Catalog**
- Removes burden of how to manually create a schema if you have a lot of tables -- but have ability to manually edit or create them yourself. 


---
# Resources
- [AWS Glue Cheat sheet](https://tutorialsdojo.com/aws-glue/)
- [AWS Glue Architecture from S3](https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/architecture.html)
- [Creating AWS Glue Databases](https://docs.aws.amazon.com/glue/latest/dg/define-database.html)
- [Capability 3. Providing secure access to data and systems for generative AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-agents.html)
- [The essential guide to building a data foundation for agentic AI](https://aws.amazon.com/data/resources/data-foundation-for-agentic-ai/)

# AWS SageMaker LLM Deployment
* This repo is devoted to all things related to using AWS SageMaker for LLM deployment.
* SageMaker provides multiple ways to deploy LLMs. This diagram below is from AWS:

![image](https://github.com/user-attachments/assets/7903b473-bb94-408b-a9d3-c3bb8e896589)


## 3 Steps to Deploy LLMs with SageMaker
* Diagram below is from AWS
1. Prepare your model
  * This includes model artifacts, container images, and IAM role mgmt.

2. Configure endpoint

3. Create Endpoint

![image](https://github.com/user-attachments/assets/be33b7ad-587a-4a55-9e70-e53915e5b47f)


## SageMaker Inference Options
* Diagram below is from AWS
  * SageMaker has a broad range of inference options.
  * Can deploy 1 to thousands of models on an endpoint.
  * Can deploy on CPU or GPUs.
  * Can go entirely serverless!


![image](https://github.com/user-attachments/assets/5bd25bbd-ba4c-4373-9a8f-f8234080240b)

### How do you select an instance type?
1. **Runtime memory (Model & sequence length)**
   * This is dependent on model size and sequence length of inference request from the LLMs.
   * **This is a VERY IMPORTANT calculation to perform before loading a model**
2. **Desired concurrency or batch sizes**
   * Increasing the BATCH SIZE will allow for more concurrent requests --> but this requires additional memory in ML instance.
3. **Response time of your application(s)**
   * Dependent upon INPUT and OUTPUT token size (e.g. payload)
   * Dependent upon hardware that drives response time:
     * AWS recommends using instances with at least A series GPUs (e.g. A10g, A100):
        * g5
        * p4
        * p5
   * Need to select instance type from above that has sufficient aggregate memory across all devices for both:
     1. Loading LLM model
     2. Making requests at runtime
    
 ### Runtime Memory Inference Calculation
 * This is the MOST IMPORTANT calculation to perform.
 * This is dependent upon the **number of parameters** and **size of each parameter**.
 * As an example for Llama-2-13B model with 2 bytes per parameter:
```
Model Size = Parameters(13-billion) x 2 bytes (FP16) = 26 GB
```
* The TOTAL memory required though to load the Llama-2-13B model is more.
  * It actually depends on input/output length, decoding strategy, model architecture, and total batch size.
* **There are other components we need to account for (source: AWS)**:
  1. Model Size --> 26 GB (we calculated this above)
  2. KV Cache --> 4 to 13 GB
     * Cached key-value tensors of the LLM take up significant memory and needs to be accounted for!
  4. Additional Memory Overhead --> 2 to 3 GB
 
![image](https://github.com/user-attachments/assets/c8c2c11e-58e3-4b1d-805a-aab6af169c4e)

### How do you calculate/account for the KV-Cache size for an LLM?
* Here we will use Llama-2-13B as an example.
* The calculation is basically broken down on a token level by....
  1. 2 times the....
  2. data type (in this case it is torch_dtype of fp16 dtype)
  3. number of hidden layers in the LLM neural network
  4. hidden size which is the dimension of the attention block
```
KV-Cache size per token = 2 * torch_dtype * num_hidden_layers * hidden_size
```

### How do you find this information and then calculate the KV-Cache?
* For open source models like Llama-2-13B we can find this in the Hugging Face repo model card.
* Go to the "Files and Versions" and find the LLM metadata file: [confg.json file](https://huggingface.co/TheBloke/Llama-2-13B-fp16/blob/main/config.json)
* From this we can see the important metadata we need:
  * `hidden_size: 5120`
  * `num_hidden_layers: 40`
* Now we can calculate the KV-Cache size per token as well as for the approximate output size we predict which is 4096 for 1 inference request (source: AWS):

![image](https://github.com/user-attachments/assets/59bccecd-1ad4-42d4-8a89-a73e511d3b0c)

### Wait, but what about more than 1 inference request at a time?
* Lets say our application is a chatbot and we predict 4 inference requests at one time, to account for the KV cache for a batch size of 4 this will change the GB result as seen here (source: AWS):

![image](https://github.com/user-attachments/assets/9d61b79b-ad71-4651-bab3-8ee4066b7337)



## Selecting an Instance Type based on Memory
* So for this model Llama-2-13B we will consider 2 instance types based on these calculations above we need a **minimum of 46 GB of memory**, so these instance types would be appropriate:
  1. `ml.g5.2xlarge` --> 4 NVIDIA GPUs & 96GB VRAM
  2. `ml.g5.4xlarge`
 
## Working with the ml.g5.12xlarge - 96GB
* With this GPU instance type we get 4 NVIDIA GPUs each with 24GB.
* You obviously can't fit a 46GB model into any 1 of these GPUs by itself because cuda will run out of memory.
  * Even if you selected a larger device such as: A100 or H100 the model still would not fit.
 
![image](https://github.com/user-attachments/assets/53ca07fa-e3a4-4a0e-a5af-284075469f87)

* You will need to SHARD the model to fit the model into 2 GPU devices. This means:
  * Number of shards = 2
  * Batch size = 4
* This will utilize 2 of the 24GB GPUs and leave 2 GPUs idle.

![image](https://github.com/user-attachments/assets/b2dd5024-d187-4c38-adfa-5670f6c85a50)


## Container Selection - Large Model Inference Container
* (Reference AWS)
1. Single container that could support TP/PP, compilation and optimization for LARGE models.
2. Optimized env with minimal setup
3. Distributed Frameworks
   * Support Hugging Face
   * NeuronX
   * DeepSpeed
   * vLLM
   * TensorRTLLM
 4. Model Server:
    * DJLServing -- multi-process execution w/ auto-scaling and UI
 5. LLM optimization
    * loading speedups
    * compilation
    * quantization is built-in
  6. Different Batch mode
     * Static/Dynamic batch
     * Continuous batching
  7. Zero code setup
     * Writing code or without writing code

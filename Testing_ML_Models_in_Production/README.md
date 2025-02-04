# Testing ML Models in Production




![image](https://github.com/user-attachments/assets/b5bf0c32-646c-4cb6-b658-5bf5fd0cf961)
* This is an excellent depiction of some of the main methods to test ML models in production. [Source](https://www.dailydoseofds.com/)


1. **A/B Testing**
   * This is usually done by dividing the incoming requests non-uniformly between the legacy model and the new candidate model or models.
   * Advantage: limits the exposure of the new candidate model/models to avoid any potential risks to your application or ML pipeline.
  

2. **Canary Testing**
  * The problem with A/B testing is it may affect all users of the application because it randomly distributes “traffic” to either model (irrespective of the user).
  * Enter "canary testing".
    * This works by exposing the new/candidate model(s) to a small subset of users in production and gradually rolled out to more users over time.
   

3. **Interleaved Testing**
  * This method involves mixing the predictions of multiple ML models in the response.
  * As an example, consider a recommendation engine at Netflix. In "interleaved" deployments, some product recommendations displayed on the Netflix homepage can come from the legacy model, and others from the candidate or new model(s).


4. **Shadow Testing**
  * All of the techniques above will affect some (or all) users of the system in production. 
  * Enter **Shadow testing** (or dark launches).
    * This allows you to test new model(s) in a production environment without affecting the user experience.
    * The candidate model(s) is/are deployed in parallel to the existing legacy model(s) and serves requests like the legacy model(s).
    * However, the output is **not sent back to the user**. Instead, the output is logged for later use to benchmark its performance against the legacy model.
        * In this technique you deploy the candidate model(s) instead of testing offline because the exact production environment can be difficult to replicate offline.
  * Overall Shadow testing offers risk-free application testing of new/candidate model(s) in a real-time production environment.


5. **Multi-Armed Bandit Testing**
  * As we saw above, usually A/B testing runs for a **defined period** based on the number of users necessary to reach a **statistically significant result**.
  * Tools such as [Evan Miller’s Awesome A/B Tools](https://www.evanmiller.org/ab-testing/sample-size.html#!15;80;5;25;1) can help you determine how large your sample size needs to be.
  * During this initial period of exploration, you evaluate whether your new model variant is going to challenge the current champion, sending traffic to the less effective variants until the test is complete, which in this case is not until week 5 (as shown in the following graph).

![image](https://github.com/user-attachments/assets/55275bdf-bcac-4b3d-9a51-d987d8812b10)


Image [source](https://aws.amazon.com/blogs/machine-learning/dynamic-a-b-testing-for-machine-learning-models-with-amazon-sagemaker-mlops-projects/)


Multi-armed bandit testing is dynamic, flexible, and allows you to introduce a gradual change from exploration to exploitation over the duration of the test, sending more traffic to the challenger variant that is delivering the highest reward as defined by your conversion metric (as shown in the following graph). 

This will reduce the traffic sent to the less effective variant over the lifetime of the testing. 

![image](https://github.com/user-attachments/assets/e74226b0-9c1e-4f7e-a74f-a6bc512b26e1)

Image [source](https://aws.amazon.com/blogs/machine-learning/dynamic-a-b-testing-for-machine-learning-models-with-amazon-sagemaker-mlops-projects/)


## Multi-Armed Bandit Testing
* In machine learning, a "multi-armed bandit" is essentially a more sophisticated version of A/B testing that leverages machine learning algorithms to dynamically allocate traffic to different variations of a product or feature, prioritizing the ones performing best in real-time, allowing for faster optimization and maximizing the desired outcome compared to traditional A/B testing where traffic is split evenly across variations throughout the experiment.
* Differences between A/B testing and MAB testing:

  1. **A/B Testing**
    * Compares two distinct versions (A and B) of a product or feature by splitting users into equal groups and measuring the performance of each variation. 
    * Provides a clear understanding of which variant is better, but can be slower as it requires a large sample size to reach statistically significant results.
 
  2. **Multi-Armed Bandit (MAB)**
    * Represents a scenario where you have multiple "arms" (variations) with **unknown reward probabilities**, and the goal is to maximize your cumulative reward by strategically choosing which arm to pull based on real-time performance data. 
    * Uses machine learning algorithms to dynamically adjust the allocation of traffic to different variations, favoring those performing better and gradually reducing exposure to underperforming variants. 
    * Focuses on maximizing the overall reward during the experiment, not just identifying the best variant with absolute certainty.
 

### When to use MAB instead of "vanilla" A/B testing
1. **Fast optimization**
   * When you need to quickly identify the best performing variant(s), especially in situations with high traffic or where user behavior can change rapidly in your application(s).

2. **Personalization**
   * When you want to tailor the experience to individual users based on their real-time behavior. 

3. **Limited data**
   * When you have a limited amount of user data and need to learn quickly. 



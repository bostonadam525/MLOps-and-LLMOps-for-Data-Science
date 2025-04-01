# Logging User Feedback in LLMOPs
* Producing consistent and accurate answers from LLMs is a major challenge.
* A very effective technique to address this issue is incorporating a robust feedback mechanism within your application to collect user feedback.
* The diagram below shows a system design I did that demonstrates how to collect logs of user feedback.
* This also demonstrates how important it is to have a system for collecting input from users and feeding that input into your online system.

![image](https://github.com/user-attachments/assets/c1c2fb47-3be2-4452-8b00-d8e431af60c9)



## Design of a logging system
* The system above was inspired by this design below [source](https://memo.d.foundation/playground/01_literature/feedback-mechanism/)

![image](https://github.com/user-attachments/assets/f6efe836-f963-4eb4-9922-2f7ad175dd20)



## Feedback Mechanisms

1. **Implicit Feedback**
* This is how users behave when they interact with your application, without them directly telling us what they think.
* There are a few main ways we can monitor and log this:
  * **Stop Generation**
    * If users stop the application (e.g. LLM) from generating a response quickly, it usually means they don’t like what it’s saying or find it irrelevant.
    * As an example, if a user reads a few lines and feel it’s not helpful, they might stop it.
    * This is also commonly noted via "Click Through Rates" (CTR) and "Page Impressions". If the users are not clicking on a generated link or page it is a logging hint the output was not relevant to them. 
  * **Double Check Responses**
    * If users go to search engines to check information from the generative AI output, it clearly demonstrates they probably don't trust the output.
    * This often happens if an LLM based app gives answers that seem false or hallucinated, especially with numbers or dates which is common when many LLMs have a cut of date of training. 
  * **Regenerate**
    * If a user requests the system to regenerate a response, it usually means they didn’t like the first output.
    * The user might use a button to get a different response when the first response doesn’t meet their liking.
    * For example, a user may want a more detailed on contextual answer with examples to their question or query.
   
2. **Explicit Feedback**
* This involves users directly communicating their satisfaction or dissatisfaction with the LLM applications responses.
* This method entails:
  * **Like/Dislike**
    * A user can give a thumbs up if they like the response or thumbs down if they don’t. This quick feedback helps us know how well the AI’s answers are working.
    * As an example, a thumbs up means the user found the output useful, while a thumbs down usually means it wasn’t helpful.
  * **Scoring**
    * Users can give a score to show how good they think the response is. This lets them give detailed feedback on whether the answer was great or just okay.
    * As an example, a 5-star rating helps you see where the LLM did well, and a 4-star rating or less shows areas for improvement.
  * **Surveys and Question**
    * These ask users specific questions about how well the LLM app is doing.
    * A user can give detailed feedback on what they like and what could be better.
    * As an example, a survey might ask about accuracy, how easy it was to use, and if the tone was right.
  * **Textual Feedback**
    * Users can write their thoughts on the LLM responses.
    * This lets them explain in detail what worked or didn’t work for them.
    * For example, the user may detail how a response helped with their work or where it missed the mark.

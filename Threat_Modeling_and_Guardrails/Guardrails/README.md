# Guardrails
- LLM guardrail frameworks are external control layers that intercept user inputs and model outputs to ensure safe, accurate, and policy-compliant AI behavior.

---
## What They Do
- **Input Validation:** Scan user prompts for jailbreaks, prompt injections, and toxic language before they reach the model.
- **PII Detection:** Mask or block sensitive data like credit card numbers, social security numbers, or API keys.
- **Topic Restriction:** Keep conversations on-brand and prevent the model from answering off-topic or restricted queries.
- **Output Filtering:** Check responses for hallucinations, bias, or harmful content, repairing or replacing malformed/unsafe text
- **Content Safety and toxicity filters:** Classify and block outputs that are violent, sexually explicit, discriminatory, or otherwise against your usage policy. VERY critical for consumer-facing deployments, regulated industries, and any AI tool accessible to a broad employee base.
- **Policy and Compliance Enforcement:** encode business and domain specific policies by restricting topics, enforce disclaimers, apply jurisdiction-specific rules, and ensure the AI never steps outside its defined operational scope.
- **Role Based Access and Context Controls:** enforce which knowledge bases, tools, or actions a given user's role can access, and they ensure that sensitive context is scoped appropriately. This is the bridge between your AI system and your existing governance infrastructure.
- **Monitoring, Logging, Audit Data:** critical layer to capture a record of every interaction with your AI/ML/LLM system — inputs, outputs, model version, timestamps, user identity, and any guardrail triggers.
  - This data serves multiple purposes: real-time alerting, post-incident forensics, and compliance audit readiness.
  - In 2026, regulators in the EU and increasingly in the US are beginning to require documented evidence of AI oversight. An audit trail is no longer optional for enterprise deployments.
- **Agentic action & tool use controls:** Agentic guardrails define which tools agents are allowed to invoke given the input reason from the LLM, require human-in-the-loop confirmation for high-stakes actions, limit blast radius (e.g., an agent can read from a database but not write to it), and enforce action-level audit logging.
- [SOURCE](https://www.elsai.ai/blog/7-types-of-ai-guardrails)

---
## Guardrail Frameworks
1. [NVIDIA NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/overview)
   - An open-source toolkit that uses a custom conversational language (Colang) to define programmable safety rules, topical boundaries, and restricted dialog flows.

2. [Guardrails AI](https://guardrailsai.com/guardrails/docs/why-use-guardrails)
   - An open-source Python library offering plug-and-play validators (using regex, classifiers, or secondary LLMs) to structurally enforce output formats like JSON/XML and block toxic content.

3. [Meta Llama Guard](https://huggingface.co/meta-llama/Llama-Guard-3-8B)
   - A series of safety classifier models trained to evaluate and label input/output content against standard harm taxonomies (like the MLCommons safety benchmark).

4. [AWS Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
   - Safety feature on AWS that blocks harmful text, filters unwanted topics, and protects private data in generative artificial intelligence applications.
   - Works as a security layer between the user and the language model. It inspects both the user's input prompt and the model's output response. It functions with models inside AWS Bedrock as well as 3rd party models such as OpenAI, Google.
   - Core Features
     - **Content Filters:** Detects and blocks harmful categories like hate speech, insults, sexual content, violence, and prompt attacks (jailbreaks).
     - **Denied Topics:** Stops the AI from discussing specific custom subjects defined by your company.
     - **Word Filters:** Blocks exact custom words or offensive phrases.
     - **Sensitive Information Filters:** Masks or redacts personal data (PII) like phone numbers or credit card numbers.
     - **Contextual Grounding Checks:** Detects hallucinations by checking if the model response matches the source text or context.
     - **Automated Reasoning Checks:** Uses mathematical logic to validate the accuracy of model answers in regulated fields.

6. [Azure AI Content Safety](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety)
   - A collection of safety and security controls in Microsoft Foundry designed to detect, block, and manage risks in generative AI models and agents.
   - Core Features:
     - **Harmful Content Filtering:** Detects and blocks hate speech, sexual content, violence, and self-harm using classification models.
     -  **Intervention Points:** Scans user inputs, tool calls, tool responses, and final model outputs.
     -  **Threat Mitigation:** Defends against direct and indirect prompt injection, jailbreaks, and hallucinations
     - **Configurable Policies:** Allows customization of severity thresholds and inclusion of custom blocklists for specific application needs.

---
# Papers
- [Dong et al, 2024. Building Guardrails for Large Language Models](https://arxiv.org/html/2402.01822v1)
- [NVIDIA Collection of Guardrails Research](https://docs.nvidia.com/nemo/guardrails/resources/research)

---
# Resources/References
- [NVIDIA Nemo Guardrails](https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/overview)

# Threat Modeling and Guardrails for LLM + Generative AI Applications
- This is a very important topic to understand in Data Science, ML and Generative AI.

---
# What is LLM Security?
- This involves identifying and mitigating LLM vulnerabilities. This includes but is not limited to their tendency to hallucinate or fabricate information. LLMs have a wide range of potential vulnerabilities, and organizations prioritize them differently based on their needs. 

- A few examples:
  - financial orgs may focus on stopping data leakage and minimizing excessive agency vulnerabilities
  - Chatbot/virtual assistant companies might prioritize addressing bias and toxic language or behaviors. 

- **If you DO NOT address these vulnerabilities it can ultimately lead to catastrophic results. For example, the spread of hallucinated or fabricated information due to insecure data and models can result in a loss of trust, legal consequences, and long-term damage to a company’s reputation and a loss of customers and profit.

---
## Four Pillars of LLM Security
- These include:
1. **Data Security**
2. **Model Security**
3. **Infrastructure Security**
4. **Ethical Considerations**

- [SOURCE](https://www.confident-ai.com/blog/the-comprehensive-guide-to-llm-security#what-is-llm-security)

<img width="7022" height="4293" alt="image" src="https://github.com/user-attachments/assets/bc9d9d7d-cf82-4f36-a7d2-3577485d334c" />

---
# OWASP Top 10 for LLM Apps in 2026
1. **LLM01: Prompt Injection** – Malicious inputs trick the model into bypassing guardrails or executing unauthorized commands
2. **LLM02: Sensitive Information Disclosure** – The model leaks confidential data, secrets, or PII present in its training or retrieval sources
3. **LLM03: Excessive Agency** – Autonomous agents are granted too much operational freedom or tool access without human oversight
4. **LLM04: Supply Chain Vulnerabilities** – Compromised third-party models, plugins, datasets, or code libraries introduce risk
5. **LLM05: Data and Model Poisoning** – Manipulated or biased training/fine-tuning data alters the core behavior of the model
6. **LLM06: Unbounded Consumption** – Resource exhaustion attacks (like Denial of Service) driven by heavy token usage or recursive loops
7. **LLM07: Misinformation** – The model outputs false, misleading, or hallucinated facts that are treated as true by users or downstream systems
8. **LLM08: Hidden Context Exposure** – Exposure of hidden system prompts, rules, or internal logic (formerly system prompt leakage)
9. **LLM09: Vector and Embedding Weaknesses** – Flaws in vector databases or embedding pipelines leading to data pollution or retrieval hijacking
10. **LLM10: Improper Output Handling** – Inadequate validation of model outputs before passing them to downstream systems or code interpreters

- Source: [OWASP LLM Top 10 (2026): What Changed and How to Test](https://hackerdna.com/blog/owasp-llm-top-10)
---

## OWASP Top 10 for LLM Apps -- Key Updates in 2026
- **Data-Informed Prioritization:** The 2026 list combines 75% expert consensus voting with 25% empirical data from real-world AI incidents.
- **Excessive Agency Promotion:** Jumped significantly higher in the ranking as autonomous agents began deploying in production environments and causing real operational impact.
- **Agentic Integration:** Formally cross-linked with the companion OWASP Top 10 for Agentic Applications and the new Agent Control Standard (ACS) for runtime enforcement.

---
# AI Threat Modeling Frameworks and Methods
1. MAESTRO
2. STRIDE
3. PASTA
4. LINDDUN
5. OCTAVE
6. VAST
7. MITRE ATLAS

- [SOURCE](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)

---
# Frameworks
- [AWS Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [AWS - Mapping to OWASP top 10 for LLM applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/owasp-top-ten.html)
- [AWS Threat Composer](https://github.com/awslabs/threat-composer)
- [DeepEval Red-Teaming LLMs](https://deepeval.com/guides/guides-red-teaming)
- [DeepEval 50+ Vulnerabilities for penetration testing](https://www.trydeepteam.com/docs/red-teaming-vulnerabilities)
- [DeepEval Adversarial Attacks testing](https://www.trydeepteam.com/docs/red-teaming-adversarial-attacks)
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)

---
# Papers
- [Ferrag et al, 2025. From Prompt Injections to Protocol Exploits: Threats in LLM-Powered AI Agents Workflows](https://arxiv.org/html/2506.23260v2)
- [Zambare et al, 2025. Securing Agentic AI: Threat Modeling and Risk Analysis for Network Monitoring Agent AI System](https://arxiv.org/html/2508.10043v1)

---
# Resources
- [Agentic AI Threat Modeling Framework: MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)
- [How To Build Threat Models For LLMs](https://medium.com/@harish_ramadoss/how-to-build-threat-models-for-llms-209d7a05298c)
- [Lasso - How to Build an AI Threat Modeling Process for Agentic Systems](https://www.lasso.security/blog/ai-threat-modeling-frameworks-for-agentic-ai)
- [Lasso - Introducing Lasso's Expanded Automated AI Red Teaming](https://www.lasso.security/blog/lasso-agentic-red-teaming)
- [LLM Guardrails for Data Leakage, Prompt Injection, and More](https://www.confident-ai.com/blog/llm-guardrails-the-ultimate-guide-to-safeguard-llm-systems)
- [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)
- [OWASP Top 10 2025 for LLM Applications: What’s new? Risks, and Mitigation Techniques](https://www.confident-ai.com/blog/owasp-top-10-2025-for-llm-applications-risks-and-mitigation-techniques)
- [OWASP LLM Top 10 (2026): What Changed and How to Test](https://hackerdna.com/blog/owasp-llm-top-10)
- [The Definitive LLM Security Guide: OWASP Top 10 2025, Safety Risks and How to Detect Them](https://www.confident-ai.com/blog/the-comprehensive-guide-to-llm-security#what-is-llm-security)

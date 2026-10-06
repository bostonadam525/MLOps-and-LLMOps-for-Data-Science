# AWS Domain-specific agent applications
- Most of this is from Module 5 of the AWS learning pathway, but there are other components mixed in.
- [Domain Specific Agents with AWS](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/domain-specific-agent-applications?trk=4dccf88d-b255-470f-82d0-13e00449c5f4&sc_channel=el)
- [github code -- Domain-Specific Agent Applications](https://github.com/aws-samples/sample-patterns-for-aws-marketplace/tree/main/agentic-ai/module5?trk=3ae467c7-b0ff-4a48-8c77-ca93c8c33017&sc_channel=em)

---
# Domain Specific 
- How to ground agents in domain specific knowledge.
- How to use guardrails and constraints.
- How to integrate into multi-agent systems.

---
## Important Components of Domain Specific Systems
- Tools + Integration
- Agent Routing
- Agent Reasoning
- Memory
- Guardrails and Safety

---
# Agentic Domain Specialization
- **The Reliability Gap: where a capable generalist agent becomes an unreliable specialist.**

## Domain Reliability
- Generalist agents are very broad and contain many silent failure modes with variable output failures. 
- **However, what production needs -- consistent correctness in specific context:**
  - **Coverage** -- depth on target domain only
  - **Reasoning** -- channeled through domain-specific patterns
  - **Consistency** -- stable across full input distribution
  - **Edge cases** -- explicit handling, measured via evaluations
  - **Threshold** -- 90-90% customer-facing | ~99% safety-critical

- **KEY POINT: domain specialization of agentic systems is NOT restrictive -- it is focusing on general reasoning in a domain through 4 deliberate levers.**

---
# 4 Levers for Domain Adaptation of Agents
- Every domain specialization operates on 1 of these 4 levers below.
- The goal is to tune these 4 levers for domain specific agents.

## 1. System Prompt
- **Primary Mechanism**
  - Domain persona
  - Priorities
  - Refusals
  - Uncertainty handling
  - Communication norms
- **Four layers:**
  - 1) Role
    2) Knowledge Context
    3) Constraints
    4) Communication
- SYSTEM PROMPT can be overridable by adversarial input -- but not sufficient alone.....

## 2. Knowledge corpus
- **Retrieval Grounding**
  - Domain specific documents, facts, policies the agent retrieves at inference via AWS bedrock knowledge bases.
  - Quality is bounded by:
    - **relevance**
    - **accuracy**
    - **freshness**
    - **coverage**
- Curation effort == prompt engineering effort
- Needs custom knowledge to act as the domain persona. 

## 3. Tool Selection
- **Capability scoring**
  - MCP-exposed tools: which of these the agent can invoke.
  - Scoping improves the quality of this (e.g. no wrong tools for domain specific tasks) AND security to limit "blast radius"
- Routing tools != deployment tools
- Scoping is VERY IMPORTANT!!!!!!!!

## 4. Guardrails
- **Unconditional enforcement**
  - What agent must NEVER do in this domain.
  - **Security Enforced constraints:**
    - Bedrock guardails
    - Patronus AI
    - Deepchecks
  - **DO NOT ENFORCE THIS WITH SYSTEM PROMPT!**
- **KEY: Must survive model reasoning attempts to overrride.**

## 5. Rule of Thumb
- If quality is affected, tune system prompt and corpus.
- If safety or liability affected, enforce with Guardrails

---
# Domain reliability thresholds
- Set your targets BEFORE you build your systems.
- Threshold dictates corpus depth, evaluation size, rollout policy.

## Internal productivity tools
- Threshold: 80-85%
- Internal productivity tools
  - users can identify and correct errors
  - low cost inconsistency
- Examples: Internal DevOps companion, code review asst, draft helper

## Customer-facing interactions
- Threshold: 90-95%
- Errors erode trust, often cannot be undone after the fact.
- Examples: Customer engagement + sales agents -- support automation, onboarding flaws, etc..

## Safety-critical domains
- Threshold: ~99%
- Incorrect output has LEGAL or FINANCIAL consequences
- Examples: medical information, finance, legal, safety routing

## KEY: Measured NOT Aspirational!
- **Thresholds must be observed on a domain representative golden dataset NOT on hand picked demo data as that is not realistic of real-world.**
- If you dont have a golden dataset, create one with SMEs, topic modeling and other techniques.

---
# Adapting the Architecture
- General prompts (eg System Prompt) sets guidelines.
- Domain prompts establish identity, knowledge context, constraints, and communication norms.

```
- Layer 1 --> Role and authority --> "contract" -- System Prompt
- Layer 2 --> Knowledge context --> corpora and information
- Layer 3 --> Behavior constraints --> what agent must always do vs. not do
- Layer 4 --> Communication norms --> tone, format, structure, etc..
```

---
## Knowledge corpus design for domain agents
- Three criteria --> Bedrock knowledge bases --> hierarchial chunking at semantic boundaries

1. **Relevance**
   - make sure corpus contains information directly useful for agents tasks.
   - Irrelevant content will reduce signal-to-noise in semantic search + retrieval
   - **How to do this:**
     - Audit corpus on regular basis (e.g. quarterly) to remove stale categories
     - Measure % of retrieved chunks actually used in responses


2. **Freshness**
   - Update the corpus when domain facts change such as:
     - prices
     - policies
     - geospatial data
     - regulatory requirements
  - **Staleness is often silent -- retrieval won't flag this.**
  - **How to do this:**
    - Tag EVERY document with `updated_at`
    - Logic to FAIL ingestion when age >30days for price/policy docs
    - Pipeline alerts on staleness

3. **Coverage**
   - Make sure corpus addresses the FULL RANGE of queries encountered including EDGE CASES and LONG-TAIL cases.
   - Most RAG failures are "no relevant chunk found" not "wrong chunk retrieved."
   - **How to do this:**
     - Always log the low-confidence retrievals
     - Cluster into coverage-gap themes
     - Use SMEs to fill-in content gaps and add metadata insights
    
4. **Chunking strategies by document type**


|Document Type| Strategy | Why |
|---|---|---|
|Narrative/policy docs | semantic chunking at paragraph or section boundaries | preserves complete, self-contained statements|
|Structured data (catalog, routes, configs)| record-level chunks (1 record = 1 chunk) | product A chunks never contaminate with product B data |
|Long hierarchical manuals | hierarchical chunking via bedrock knowledge bases | parent-child surface fact AND broader context|


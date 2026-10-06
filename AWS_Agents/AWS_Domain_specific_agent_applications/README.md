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

---
# Customer Facing Agents
- **Use Intent as entry point** --> every customer interaction begins with a **classification problem** -- answer determines retrieval, tools, tone, and scope.
- Deterministic vs. Semantic intent

## Escalation Design
- No customer engagement agent ships without a HANDOFF policy -- usually 3 trigger categories and context-preserving transfer via Amazon Connect.

1. **Scope escalation**
   - customer request falls outside agents authorized scope
   - Detection signals:
     - intent classification confidence high
     - intent matches an out of scope category
     - example: legal commitment, pricing overrride

2. **Sentiment escalation**
   - customer tone indicates distress, frustration, or dissatisfaction requiring human interaction
   - Detection signals:
     - Sentiment analysis on latest turn
     - Repeated negative sentiment across turns
     - Explicit distress keywords/phrases

3. **Complexity escalation**
   - Agent confidence in its own response falls below domain reliability threshold
   - Detection threshold:
     - Retrieval confidence below threshold
     - Generation self-consistency check failed
     - Multi-turn reasoning loop exceeded

### Context-preserving handoff via Amazon Connect
- if escalation fires, agent passes full conversation context -- issue classification, sentiment, account data to connect agent workspace.
- Human then continues.
- Useful for contact center operations. 

---
# Location Aware Agents
- Why location agents need tools not training.
- LLMs know where most geographic locations are, but they can't compute optimal route among multiple stops in a time-window and capacity constraints.
- **Design principle:**
  - Use model for natural language understanding (NLU), intent interpretation, and result synthesis.
  - Use geospatial tools for all spatial data access and computation.
  - Boundary must be explicit and enforced through tool schema. 

## Tools in AWS -- MCP 
- Mapbox location services
- Amazon location service

## Freshness and caching in geospatial contexts
- Not all geospatial data has same freshness requirement -- cache slow moving data, fetch fresh data in real-time.

1. **Static -- cache aggressively**

2. **Semi-static -- cache with care**

3. **Real-time -- never cache!**

4. **DO NOT CACHE TRAFFIC DATA**
   - operational concerns

---
# Voice-enabled Agents

## Voice enabled agent pipeline
- There are 4 stages.
- Streaming at every boundary
- Total perceived latency <= 1-2 seconds (avoids customer frustration)

1. **Speech --> Text**
   - Amazon  Transcripe, Deepgram

2. **Intent + Reasoning**
   - Bedrock agent domain prompt

3. **Text --> Speech**
   - Amazon Polly, Deepgram TTS

4. **Audio delivery**
   - Amazon kinesis streaming
  
---
# Domain specific Guardrails -- enforce at infrastructure, not in the prompt
- **Key point: System prompt constraints can easily be injected and talked around. Bedrock Guardrails, Patronus AI, and Deepchecks enforce unconditionally.**
- Examples:

1. **Customer Engagement**
   - Price guarantees: never commit to prices not verified in real-time from catalog
   - Regulated disclosures: require specific disclosure text when mentioning regulated products
   - PII detection: built-in PII redaction on inputs AND outputs via Bedrock Guardrails.
   - Authority limits: hard block on commitments outside authorized scope.
   - Sentiment escalation: automatic human routing for distress signals.

2. **Location and logistics**
   - Confidence thresholds: present as estimage when route confidence <= threshold
   - Data freshness: max age of geospatial data enforced per tool type.
   - Coverage boundaries: block recommendations in areas with inadequate data coverage.
   - Liability disclaimers: auto-append for recommendations with significant uncertainty.
   - Safety routing: never recommend against local traffic laws or restrictions.
  

3. **Voice interface**
   - Format enforcement: block markdown, HTML, code blocks in voice mode
   - Length caps: max response words/duration per interaction turn
   - Language match: block cross-language responses unless requested
   - Interrupt safety: require safe handling of partial commands in interruption.
   - Transcription confidence: auto-clarify when STT confidence below threshold.

4. **KEY PRINCIPLE**
   - **If it affects your liability, compliance, or safety --- it does not live in the system prompt it lives in Bedrock Guardrails where model reasoning CANNOT override it.**
  
---
# Domain Specific Evaluation -- beyond generic quality signals
- Bedrock AgentCore Evaluations
- Custom evaluators
- Domain experts in loop

1. **Build domain-representative golden dataset**
   - Draw this from actual input distributions NOT engineering assumptions.
   - Pull from REAL CUSTOMER SUPPORT TICKETS, chat logs, call recordings, routing requests
   - Include common requests, common edge cases AND common failure modes/problems/issues
   - **DO NOT hand-construct what engineers think users will ask**
   - Annotate with domain-expert involvement
  
2. **Automate high-volume layer -- human-review edge cases**
   - LLM-as-judge with domain rubrics + schema validation + automated fact-checking
   - Automated evaluators run continuously on every deployment + every N% of production traffic
   - Flag responses below threshold on objective criteria
   - Human experts review flagged responses + contribute annotations back
   - Bedrock AgentCore evaluations support custom evaluators for domain-specific rubrics

3. **Close the loop -- annotations become new test cases**
   - Evaluation system improves as agent is used in production!
   - Every expert annotation is a candidate test case
   - Production failures surface new evaluation dimensions
   - Golden dataset grows along axes that actually matter
   - Quality gate tightens over time without manual spec rewrites
  
4. **Common Problem**
   - General agent at 92% on hand-picked dataset can fail up to 75% on domain-specific distribution.
  

# AWS Multi-Agent Architectures
- Most of this is from Module 3 of the AWS learning pathway, but there are other components mixed in.
- [Multi-agent architectures on AWS](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/multi-agent-architectures?trk=4dccf88d-b255-470f-82d0-13e00449c5f4&sc_channel=el&refid=bf3e7bdd-12f2-4e8b-a20f-efc016685f96)
- [AWS Github multi-agent architecture templates](https://github.com/aws-samples/sample-patterns-for-aws-marketplace/tree/main/agentic-ai/module4?trk=c6216683-9cff-4741-9f17-23908a5ea8ab&sc_channel=em)

---
# 13 capability domains to build production-ready agentic systems
- This is the architecture that defines what every production ready agentic system must address as defined by AWS:

<img width="847" height="478" alt="Screenshot 2026-10-01 141353" src="https://github.com/user-attachments/assets/7d3de625-ec7d-4f8a-852f-bf54f431e88c" />


---
# Why do you need multi-agents -- case for collaborative AI systems
- There are 4 important "triggers" to consider when to move from a single-agent system to a multi-agentic system:

1. **Context Saturation**
   - COMPLEX long-horizon tasks that overflow a single context window.
   - Agent often forgets work it did earlier but does not know it has.

2. **Task specialization**
   - 1 agent is trying to excel at multiple things AT THE SAME TIME: 
     - a) Security
     - b) Infrastructure-as-code (IaC)
     - c) CI/CD

  - This leads to mediocre answers/responses and results rather than specific domain excellence.


3. **Latency and Parallelism**
   - Sequential task execution is SLOW and/or delayed.
   - Independent subtasks (e.g. security audits, cost estimates, compliance checks) -- RUN IN PARALLEL to avoid delays!

4. **Fault Isolation**
   - Single-agent system derails ENTIRE workflow.
   - Multi-agent systems localize failures --> 1 agent not working does not hinder the rest of the system.

5. **RULE OF THUMB**
   - Move to multi-agent systems when a single-agent workflow shows any 2 of these 4 triggers at the SAME TIME.

---
# Multi-Agent Systems -- Anatomy
- Every Multi-Agent system regardless of the purpose or number of agents is organized around these 4 planes below.
- If you don't include these 4 planes it will make it difficult to debug and trace your system. 

1. **Control Plane** -- orchestration
   - **KEY: Orchestrator directs, it DOES NOT execute. If you delegate tasks beyond orchestration to an orchestrator it is asking for trouble.**
2. **Execution Plane** -- specialized agents
   - **KEY: Independence is the key here. Think of "microservices" but for Agents.**
3. **State Plane** -- shared memory
   - **KEY: Shared memory, information, and augmented knowledge shared among agents.**
4. **Capability plane** -- Tools and MCP

<img width="790" height="417" alt="Screenshot 2026-10-01 152958" src="https://github.com/user-attachments/assets/cfb8b25f-9fb9-4322-af86-09a3b1465703" />


---
# 4 Orchestration Patterns for Multi-Agents
1. **Centralized Orchestration**
   - **Most flexible pattern**
   - **Problem: A centralized single point orchestrator though can create bottlenecks so be careful!**
2. **Skill-based dispatch**
   - Skills are dynamic and easily invoked by reasoning agent -- makes them easy to access and easy to test and validate.
   - **Problem --> open ended tasks this is not ideal, especially if there are skills that you do not account for in your agentic workflow. This is best for STABLE WELL-DEFINED workflows.**
3. **Handoff chains**
   - Each agent hands off to the next agent.
   - **Problem: Rigidity! Branching logic can become a big problem over time.**
4. **Parallel fan-out and synthesis**
   - Router dispatches multiple domain tasks to multiple specialists --> aggregate or synthesize the results of each agents findings.
   - **Problem: Start simple and move to more complex when necessary.**

<img width="760" height="432" alt="Screenshot 2026-10-01 153734" src="https://github.com/user-attachments/assets/2a606f70-905b-41a0-99ba-7c647b2ee259" />


---
# Non-determinism compounds across agent boundaries
- The diagram below from AWS shows us the big problem with multi-agent architectures which is that:

```
In a multi-agent pipeline when 4 agents produce correct output 90% of the time the probability of correct output from the agentic pipeline is only 66%...

```

<img width="760" height="429" alt="image" src="https://github.com/user-attachments/assets/d55ea588-98dd-4d24-bf44-51c4b06dfaea" />



## How do we defend against propagation?
- Individual agent accuracy must be BETTER than your overall error rate. So, to achieve this you should consider:

1. **Structured schema at every boundary**
   - Require JSON-schema validation outputs at every handoff.
   - Free-form inter-agent prose is a bug.
   - AWS Bedrocks structured output + Claude's native JSON constraints enable this without sacrificing reasoning quality.

2. **Abstention as a feature**
   - Agents uncertain about a task should return a structured abstention response -- NOT a low confidence guess. **If agent doesn't know answer it should say "I don't know" rather than low confidence errors.**
   - Build and evaluate abstention behavior in golden datasets that you build overtime from data.

3. **End-to-end evaluation (NOT-OPTIONAL)**
   - Per-agent evals are NECESSARY but not sufficient enough --> **Run COMPLETE agentic workflow evaluations!**
   - AWS Bedrock AgentCore evaluations are built-in. The `GoalSuccessRate` measures system-level success, NOT per-agent output quality. 

---
# Shared Context and Knowledge Exchange
- This is how agents share information across boundaries.
- There are 4 types of data to know about here:

1. **Task state**
   - **Type:** Durable
   - **Example**: Amazon DynamoDB
   - **Purpose:** Provides full audit trail

2. **Session Context**
   - **Type: Short-lived**
   - **Example: Amazon ElastiCache**
   - **Purpose: Recently accessed payloads, millisecond access matters.**
  
3. **Domain knowledge**
   - **Type: Read-heavy**
   - **Example: Amazon Bedrock Knowledge Bases**
   - **Purpose:** Vector search/retrieval, data governance shared across all agents, NO duplication
  
4. **Intermediate results**
   - **Type:** Archival
   - **Example:** Amazon S3
   - **Purpose:** Cost-effective, durable, referenced by task state in DynamoDB.
  
5. **Important Handoff payload principle:**
   - Include what the next agent needs -- nothing more!!
   - Verbose payloads bloat context windows and degrade reasoning quality. 

---
# MCP vs. Agent to Agent (A2A) -- Different problems, different protocols
- These are not the same and therefore we should discuss their differences and unique use cases.


## MCP (Model Context Protocol)
- **Agent --> Tool Interface**
- This provides the **client-server** protocol:
  - **Agent is always the client**
  - **Tool server is always responder**
 
- MCP provides **standardized, discoverable, schema-validated tool interfaces**

- **Multi agent-MCP:**
  - server must implement per-agent access controls at server level -- NOT in system prompts


- Tool schema quality directly determines agent behavior quality.

- **Version-controlled:**
  - Tracks MCP server version in each agent's config.
  - Test before updating in production!!!


## Agent-to-Agent Protocol (A2A)
- **Agent --> Agent interface**
- Peer Protocol:
  - Any agent cant initiate or receive -- symmetric
  - Unlike MCPs client-server model
 
- **Task objects carry:**
  - Description
  - Context
  - Authorized resources
  - Expected output schema
  - Constraints
 
- **Agent Cards:**
  - Structured capability declarations at known endpoints
  - This enables dynamic discoverability without pre-built integration
 
- **A2A expands attack surface:**
  - Validate task objects against schemas
  - **Apply AWS Bedrock Guardrails at every A2A boundary**

- **Do not use MCP for agent-to-agent delegation**
  - It is the wrong use case and abstraction...

---
# Security for Multi-Agent Systems
- These are IMPORTANT concerns as we see below and how to handle them:

<img width="819" height="461" alt="Screenshot 2026-10-01 163304" src="https://github.com/user-attachments/assets/d7469973-76ea-4b36-9270-4dea4cc62d4f" />

---
# What are the 4 Failure Modes UNIQUE to Multi-Agent Systems?
1. **Cascading failures**
2. **Orchestration loops**
3. **Conflicting parallel outputs**
4. **Context corruption at handoffs**

<img width="818" height="454" alt="Screenshot 2026-10-01 163547" src="https://github.com/user-attachments/assets/d5094cb8-f7ae-4c26-94d8-7419b71ba6ba" />

---
## Key: Distributed Observability across agent boundaries
- There are multiple tools available on AWS:

1. Amazon CloudWatch traces
   - Allows tracing across Lambda, Bedrock agent invocations, and Step functions.
   - Renders full execution as single navigable trace.

2. LangSmith
3. LangFuse
4. Layered Evaluation Strategy


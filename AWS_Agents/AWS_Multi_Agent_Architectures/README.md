# AWS Multi-Agent Architectures
- Most of this is from Module 3 of the AWS learning pathway, but there are other components mixed in.
- [Multi-agent architectures on AWS](https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/multi-agent-architectures?trk=4dccf88d-b255-470f-82d0-13e00449c5f4&sc_channel=el&refid=bf3e7bdd-12f2-4e8b-a20f-efc016685f96)

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
2. **Skill-based dispatch**
3. **Handoff chains**
4. **Parallel fan-out and synthesis**

<img width="760" height="432" alt="Screenshot 2026-10-01 153734" src="https://github.com/user-attachments/assets/2a606f70-905b-41a0-99ba-7c647b2ee259" />






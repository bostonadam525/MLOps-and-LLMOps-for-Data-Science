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
   - 

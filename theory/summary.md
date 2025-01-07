# Lecture 1: Introduction to Agents and Multi-Agent Systems (MAS)

## Overview
This lecture introduces the foundational concepts of agents and Multi-Agent Systems (MAS), emphasizing their distinct characteristics, applications, and interdisciplinary nature.

---

## 1. Main Trends in Computer Science
### Key Trends
1. **Ubiquity:** 
   - Computing power is embedded in everyday devices (e.g., IoT, smartwatches).
   - Leads to ubiquitous and adaptive intelligence.

2. **Interconnection:**
   - Systems are networked, exemplified by the Internet and Semantic Web.
   - Focus on interaction-driven computing models.

3. **Intelligence:**
   - Increasing automation of complex tasks using domain knowledge and inference.

4. **Delegation:**
   - Computers autonomously perform tasks (e.g., self-driving cars, adaptive cruise control).

5. **Human-Oriented Programming:**
   - Transition toward abstractions aligning with human understanding (e.g., agent-oriented software engineering).

---

## 2. Agents and Multi-Agent Systems
### **Definition of an Agent**
- A computational system capable of independent action in a dynamic environment to achieve objectives.
- Properties include autonomy, adaptability, and intelligent decision-making.

### **Definition of Multi-Agent Systems**
- Comprise multiple interacting agents.
- Require cooperation, coordination, and negotiation among agents with diverse goals.

---

## 3. Objections to MAS
### Key Misconceptions:
1. **“Isn't it just Distributed/Concurrent Systems?”**
   - MAS agents are autonomous and self-interested, requiring unique synchronization and negotiation mechanisms.

2. **“Isn't it just AI?”**
   - MAS integrates social aspects of agency ignored in classical AI.

3. **“Isn't it just Economics/Game Theory?”**
   - While inspired by these fields, MAS focuses on computational, resource-bounded agents.

4. **“Isn't it just Social Science?”**
   - MAS takes inspiration but focuses on designing artificial societies rather than replicating human societies.

---

## 4. Agents vs Related Technologies
### Comparison with Objects:
- **Objects:** Passive, reactive, non-autonomous.
- **Agents:** Active, autonomous, proactive, and intelligent.

### Comparison with Expert Systems:
- **Expert Systems:** Disembodied, single-domain expertise.
- **Agents:** Situated in environments, capable of action, and designed for cooperation.

---

## 5. Viewpoints on Agent Technology
### Roles of Agents:
1. **Design Paradigm:**
   - Modular and reusable components for complex systems.
2. **Technology Source:**
   - Techniques for balancing reaction and deliberation, learning, negotiation, and coalition formation.
3. **Social Simulation:**
   - Understanding societal processes through MAS models.

---

## Applications of MAS
1. **Spacecraft Control:**
   - Autonomous probes capable of handling unexpected events (e.g., NASA’s DS1).
2. **Air Traffic Control:**
   - Autonomous systems cooperate to manage flights in the absence of human controllers.
3. **E-Personal Assistants:**
   - Perform tasks like planning, negotiating, and purchasing on behalf of users.

---

## Interdisciplinary Nature of MAS
- Influenced by fields like economics, philosophy, game theory, logic, and social sciences.
- Emphasizes computational agents distinct from purely theoretical models.

---

## Research on MAS
- **Organizations:** IFAAMAS.
- **Conferences:** AAMAS, PAAMS.
- **Journals:** *Autonomous Agents and Multi-Agent Systems* (Springer).

---

## Suggested Readings
1. Chapter 1: *An Introduction to Multi-Agent Systems* by M. Wooldridge.
2. Initial part of Chapter 1: *Agentes software y sistemas multi-agente* by A. Mas.

---


# Lecture 2: Agent Architectures

## Overview
This lecture explores the architectures of intelligent agents, focusing on their definitions, types of environments, and the three main architectural paradigms: reactive, deliberative, and hybrid.

---

## 1. Definition of an Intelligent Agent
- **Agent Definition:** A system that perceives its environment through sensors and acts upon it using effectors to achieve goals.
- **Autonomous Agent:** Situated within an environment, acting independently to fulfill tasks and adapt to changes over time.

---

## 2. Types of Environments
1. **Accessible vs Inaccessible:**
   - **Accessible:** Complete, accurate, up-to-date information is available.
   - **Inaccessible:** Common in real-world applications, making agent design more complex.

2. **Deterministic vs Non-Deterministic:**
   - **Deterministic:** Actions lead to predictable outcomes.
   - **Non-Deterministic:** Outcomes are uncertain, complicating design.

3. **Episodic vs Non-Episodic:**
   - **Episodic:** Performance depends on independent episodes.
   - **Non-Episodic:** Requires reasoning across episodes.

4. **Static vs Dynamic:**
   - **Static:** Unchanging unless acted upon by the agent.
   - **Dynamic:** Changes beyond the agent's control.

5. **Discrete vs Continuous:**
   - **Discrete:** Fixed, finite actions and percepts.
   - **Continuous:** Real-world environments, more complex.

---

## 3. Agent Architectures
### **General Concept**
- **Architecture:** A methodology for building autonomous agents, specifying:
  - Decomposition into component modules.
  - Interaction between modules to process sensor data, internal states, and actions.

---

### **3.1 Reactive Architectures**
- **Features:**
  - No or minimal internal world representation.
  - Direct coupling of perception and action.
  - Intelligence emerges from interactions with the environment.
  - Example: Ant colonies using pheromones to discover shortest paths.
  
- **Advantages:**
  - Simplicity, flexibility, low computational cost.
  - Robustness and adaptability in dynamic environments.

- **Limitations:**
  - Lack of long-term planning capabilities.
  - Difficulty incorporating non-local information or learning.

---

### **3.2 Deliberative Architectures**
- **Features:**
  - Explicit symbolic world models.
  - Decisions based on logical reasoning (sense-plan-act paradigm).
  - Example: Belief-Desire-Intention (BDI) model:
    - **Beliefs:** Agent's understanding of the world.
    - **Desires:** Potential goals (realistic and consistent subset).
    - **Intentions:** Goals committed to by the agent.

- **Advantages:**
  - Capable of long-term planning and symbolic reasoning.
  
- **Limitations:**
  - High computational cost.
  - Inefficiency in dynamic environments due to constant model updates.

---

### **3.3 Hybrid Architectures**
- **Features:**
  - Combine reactive and deliberative components.
  - Use layered structures where reactive layers often take precedence.
  - Examples:
    1. **TOURINGMACHINES:** Integrates perception, action, and three control layers (reactive, planning, modeling).
    2. **InteRRaP:** Vertically layered with behavior, planning, and cooperative planning layers.

- **Advantages:**
  - Balances fast reactivity and complex planning.
  - Suitable for dynamic and complex environments.

- **Limitations:**
  - Lack of general design methodologies.
  - Application-specific and unsupported by formal theories.

---

## Critiques and Challenges
- Reactive systems are unsuitable for tasks requiring global knowledge or long-term planning.
- Deliberative systems struggle with dynamic, rapidly changing environments.
- Hybrid architectures lack standardized design methodologies and are often tailored for specific applications.

---

## Suggested Readings
1. Chapter 5: *An Introduction to Multi-Agent Systems* by M. Wooldridge.
2. Chapter 2: *Agentes software y sistemas multi-agente* by A. Mas.

---


# Lecture 3: Agent Properties and Types - Multi-Agent Systems

## Overview
This lecture explores the various properties and types of agents, emphasizing their classification, specific functionalities, and mechanisms to "agentify" applications for use in multi-agent systems (MAS).

---

## 1. Agent Properties
### **Key Properties**
1. **Flexibility:** Ability to adapt and act proactively in dynamic environments.
2. **Reactivity:** Responds to environmental changes in a timely and appropriate manner.
3. **Proactiveness:** Goal-oriented behavior, capable of taking initiative and recognizing opportunities.
4. **Social Ability:** Interacts with other agents or humans using agent communication languages.
5. **Rationality:** Acts to achieve goals without contradictory actions, based on its beliefs.
6. **Reasoning:** Distinguishes intelligent agents through planning, inferring, and extrapolating knowledge.
7. **Learning:** Improves performance over time via experience and adaptation.
8. **Autonomy:** Operates independently, pursuing goals without continuous user commands.
9. **Temporal Continuity:** Continuously running processes, either active or passive.
10. **Mobility:** Moves across networks to perform tasks locally, then returns with results.

### **Relationships Between Properties**
- More learning enhances flexibility and autonomy.
- Increased reasoning improves rationality and proactiveness.
- Reduced autonomy limits proactiveness.

### **Core Properties for MAS**
- Autonomy, reactivity, reasoning, learning, and communication.

---

## 2. Agent Types
### **Classifications**
1. **By Properties:** E.g., reasoning, mobility, flexibility.
2. **By Purpose:** Collaborative, interface, information, facilitator agents.

### **Key Types**
1. **Collaborative Agents:** 
   - Emphasize communication and cooperation in open MAS environments.
   - Solve distributed problems (e.g., healthcare, air-traffic control).

2. **Interface (User) Agents:**
   - Act as personal assistants, learning user preferences to perform tasks (e.g., mail management, scheduling).

3. **Information Agents:**
   - Manage and synthesize data from distributed information sources (e.g., web crawling, personalized data integration).

4. **Facilitator Agents:**
   - Mediate communication and resource discovery in federated systems (e.g., RETSINA framework).

---

## 3. Agentification Mechanisms
### **Approaches**
1. **Translators:** Bridge applications with MAS using external communication protocols.
   - Pros: No code modification, reusable.
   - Cons: Less efficient than wrappers.

2. **Wrappers:** Modify application code to enable direct MAS communication.
   - Pros: High computational efficiency.
   - Cons: Requires access to source code, not reusable.

3. **Re-Coding:** Rewrite applications as agents from scratch.
   - Pros: Optimized performance.
   - Cons: High effort and resource-intensive.

### **Applications**
- Integration of legacy systems into MAS for added functionality.

---

## Final Remarks
- Different types of agents are often combined in MAS, though not all types are necessary for every application.
- Learning and communication remain pivotal to agent effectiveness in dynamic and distributed systems.

### **Recommended Materials**
- *An Introduction to Multi-Agent Systems* by M. Wooldridge (Chapter 2, Section 10.3).
- Example frameworks: RETSINA (collaborative agents), HeCaSe (personalized medical services).



# Lecture 4: Agent Communication - Multi-Agent Systems

## Overview
This lecture, part of the Multi-Agent Systems (MAS) course, focuses on agent communication within distributed problem-solving systems. It highlights the foundational concepts, mechanisms, and protocols that enable agents to interact and collaborate effectively.

---

## Course Structure
### **First Part: Agents**
- Introduction to agent technology
- Agent architectures, properties, and types

### **Second Part: Multi-Agent Systems**
- Topics include:
  - Agent communication
  - Coordination
  - Negotiation
  - Distributed planning
  - Coalition formation
  - Application domains

---

## 1. Definition of a Multi-Agent System
### **Key Characteristics**
- A collection of deliberative, autonomous, collaborative agents.
- Solves complex distributed problems using communication and cooperation.

### **Benefits**
- **Modularity:** Simplifies problem-solving by breaking problems into manageable sub-problems.
- **Efficiency:** Achieves faster solutions through concurrency and partial result sharing.
- **Reliability:** Avoids single points of failure through redundancy and dynamic redistribution.
- **Flexibility:** Dynamically creates/deletes agents, generates subtasks, and forms coalitions.

---

## 2. Distributed Problem Solving
### **Core Requirements**
1. **Coherence:** Agents must be willing to collaborate.
2. **Competence:** Agents must know how to collaborate.
3. **Coordination:** Agents must follow a shared plan.

### **Steps**
1. **Task Decomposition:** Dividing a complex problem into sub-tasks.
2. **Task Allocation:** Assigning tasks dynamically, often using protocols like Contract Net.
3. **Task Accomplishment:** Agents execute tasks, managing dependencies and potential conflicts.
4. **Result Synthesis:** Combining results into a complete solution, potentially resolving conflicts.

---

## 3. Agent Communication
### **Importance**
- Facilitates distributed problem-solving.
- Supports coordination, cooperation, and information sharing.

### **Communication Types**
- **Point-to-Point:** Direct interaction between agents.
- **Broadcast:** Sharing information with a group.
- **Mediated:** Third-party facilitation (e.g., facilitators or directories).

### **Methods**
1. **Blackboard Systems:** Centralized shared information space.
   - **Advantages:** Flexibility and independence from agent architecture.
   - **Disadvantages:** Centralized bottleneck and single point of failure.
2. **Message Passing:** Direct information exchange, often framed as "speech acts."
   - Based on **Speech Act Theory** (e.g., inform, request, promise).

---

## Communication Protocols
### **Standards**
- **FIPA (Foundation for Intelligent Physical Agents):**
  - Defines communication languages (FIPA-ACL) and protocols.

### **Examples**
1. **Contract Net Protocol:** Task-sharing mechanism.
   - **Stages:** Recognition, Announcement, Bidding, Awarding, Expediting.
   - **Features:** Mutual selection, dynamic transfer, local evaluation.
   - **Limitations:** Non-trivial problem decomposition, solution synthesis, and computational overhead.
2. **FIPA-Request/Query Protocols:** Facilitate structured dialogue for task requests or information queries.

---

### Contract Net Protocol (Expanded)

The **Contract Net Protocol (CNP)** is a task-sharing mechanism within multi-agent systems that provides a structured way for agents to allocate and accomplish tasks collaboratively. It supports dynamic task allocation through mutual agreements between managers (agents needing help) and contractors (agents offering services). Below is an expanded explanation of its stages, features, and challenges.

#### **Stages of the Contract Net Protocol**

1. **Recognition**  
   - A manager agent identifies a task that requires external assistance.  
   - This need may arise from limitations in capability, resource constraints, or preferences for improved efficiency or quality.  

2. **Announcement**  
   - The manager broadcasts a task announcement specifying the task details, constraints (e.g., deadlines, required quality), and any meta-task preferences.  
   - This stage ensures all potential contractors are informed of the opportunity.

3. **Bidding**  
   - Interested contractor agents evaluate the task based on their capabilities, resource availability, and competing priorities.  
   - Agents submit bids, detailing the terms under which they can perform the task (e.g., cost, expected completion time).  

4. **Awarding**  
   - The manager evaluates received bids based on predefined criteria, such as cost-efficiency, reliability, or quality.  
   - The contract is awarded to the most suitable contractor, and the decision is communicated to all participants.

5. **Expediting**  
   - The contractor executes the task and may further subcontract portions of it if needed.  
   - This stage may involve monitoring progress and ensuring compliance with the agreed terms.

#### **Key Features**

- **Mutual Selection:**  
  - Contractors autonomously decide whether to bid.  
  - Managers independently evaluate and choose among bids, ensuring flexibility and autonomy.

- **Dynamic Transfer:**  
  - Tasks and responsibilities can be reallocated dynamically to adapt to changing conditions.  
  - This flexibility supports fault tolerance and resource optimization.

- **Local Evaluation:**  
  - Decisions are made locally by individual agents, preserving autonomy and privacy.

#### **Challenges and Limitations**

- **Complex Problem Decomposition:**  
  - Effective decomposition of a problem into manageable tasks is a non-trivial step, especially when tasks are interdependent.

- **Solution Synthesis:**  
  - Integrating results from multiple contractors can be challenging due to conflicts or inconsistencies in partial solutions.

- **Computational Overhead:**  
  - Managing communication, evaluating bids, and waiting for responses introduce delays and increase the system's computational load.

- **Quality of Service (QoS):**  
  - Determining appropriate criteria for task specification and bid evaluation requires careful design to ensure service quality.

#### **Efficiency Enhancements**

1. **Focused Addressing:**  
   - Instead of broadcasting to all agents, announcements can target specific, relevant agents based on past interactions or task specialization.

2. **Directed Contracts:**  
   - Managers with prior knowledge of suitable agents can directly assign tasks, reducing deliberation time.

3. **Proactive Offers:**  
   - Contractors may proactively inform managers of their capabilities and readiness to handle specific tasks, streamlining future announcements.

#### **Applications in MAS**

The Contract Net Protocol is widely used in domains requiring dynamic, decentralized task allocation, such as logistics, manufacturing, and robotics. Its flexibility and scalability make it a valuable tool for distributed problem-solving in multi-agent systems.

For further exploration, consider reading chapters 6 and 7 of Wooldridge’s *Introduction to Multiagent Systems*.

---

## Recommended Reading
- Chapters 6 and 7 of Wooldridge’s *Introduction to Multiagent Systems*.

---

This lecture emphasizes the interplay between agent autonomy, communication, and cooperation to address distributed, complex problems effectively in MAS contexts.

# Lecture 5: Cooperation in MAS (I) – PGP & GPGP

## Overview
This lecture introduces the concept of coordination and cooperation in Multi-Agent Systems (MAS). It emphasizes the principles of emergent behavior, explicit communication, Partial Global Planning (PGP), and Generalized Partial Global Planning (GPGP).

---

## Coordination
### **Definition**
"Coordination is the process by which an agent reasons about its local actions and the (anticipated) actions of others to ensure coherent behavior in the community." – N. Jennings, 1996.

### **When to Use Coordination**
- Choices in actions affect agent performance or others.
- Dependencies between sub-problems require solving in specific orders.
- Sharing partial solutions can simplify other sub-problems.

### **Components**
1. Deciding agent activities and timing.
2. Determining what, when, and to whom to communicate.
3. Balancing domain and control information.

### **Factors Influencing Coordination**
- Information availability and cost.
- Importance of optimal solutions versus real-time constraints.
- Trade-offs between computation costs and system performance.

---

## Cooperation Hierarchy
### **Benevolent Agents**
- Agents always help others when requested.
- Simplifies design by assuming mutual interests.

### **Self-Interested Agents**
- Agents act in their own interest, often leading to conflicts.
- Common in competitive environments like e-commerce.

### **Emergent Behavior**
- Agents unintentionally cooperate, leading to complex system behavior without explicit coordination (e.g., stone-gathering robots).

### **Cooperative Agents**
- Explicit cooperation through communication (e.g., messages, blackboards).
- Implicit cooperation by observing and reacting to others' behavior.

![Cooperation Hierarchy](figures/Cooperation%20Hierarchy.png)

---

## Partial Global Planning (PGP)
### **Overview**
- Developed by Durfee & Lesser for Distributed Vehicle Monitoring (DVM).
- Integrates planning and execution in inherently distributed tasks.

### **Phases**
1. **Create Local Plans:**
   - Each agent generates a sequence of actions for assigned tasks.
   - Plans are modifiable and account for action duration and quality.
![Local Plan](figures/Create%20Local%20Plans.png)

2. **Exchange Local Plans:**
   - Agents share relevant plans with others based on system structure.
3. **Generate Partial Global Plans:**
   - Combine local plans into a global activity map.
   - Identify sub-goals and opportunities for better coordination.
4. **Optimize Partial Global Plans:**
   - Reorder tasks, reallocate work, and adjust plans based on authority or redundancy.
5. **Building the Solution:**  
   From the modified Plan Activity Map, each agent builds a Solution Construction Graph: how the agents should interact, including specifications about:  
   - What partial results to exchange  
   - When to exchange them  
   - Who to exchange them with


### **Benefits**
- Dynamic adaptation to environmental changes.
- Enhanced efficiency through shared work and reduced duplication.

### **Drawbacks**
- Complexity in data structure management.
- Originally domain-specific to DVM.

---

## Generalized Partial Global Planning (GPGP)
### **Key Features**
- Modular coordination mechanisms for dynamic task scheduling.
- Domain-independent, except for initial task relationship determination.

### **Task Relationships**
- **Enablement:** Task A must precede Task B.
- **Facilitation:** Task A improves Task B's quality or speed.
- **Hindrance:** Task A negatively impacts Task B's quality or speed.
- **Structure**: AND-OR Tree:
    - AND -> Sub-problems.
    - OR -> Redundancy

### **Agent Structure**
1. **Belief Database:** Stores task structure information.
2. **Coordination Mechanisms:** Analyze task relationships and impose constraints.
3. **Local Scheduler:** Builds schedules considering commitments and constraints.

### **Coordination Mechanisms**
1. **Update Non-Local Viewpoints:** Share task information between agents.
2. **Manage Hard Coordination Relationships:** Ensure timely task execution to avoid bottlenecks.
3. **Manage Soft Coordination Relationships:** Optimize for quality and speed when possible.
4. **Detect Redundancy:** Resolve duplicate efforts by assigning tasks to the most suitable agent.
    Strategies such as Random Choice, Fastest solution, best solution, less assigned tasks.

### **Conclusions**
- Flexible coordination adaptable to dynamic environments.
- Enables efficient task distribution and agreement on final plans.

---

## Suggested Readings
- Chapter 8, *An Introduction to Multi-Agent Systems* by M. Wooldridge.
- Chapter 4, *Agentes Software y Sistemas Multi-Agente* by A. Mas.
- Papers on cooperation hierarchy and Distributed Partial Global Planning by Decker & Lesser.

# Lecture 6: Cooperation in MAS (II) – Coalition Formation

## Overview
This lecture delves into coalition formation as a mechanism for cooperation among deliberative agents in Multi-Agent Systems (MAS). It builds on previous concepts like distributed planning and explores how agents form temporary collaborations to achieve tasks efficiently.

---

## What is a Coalition?
- **Definition:** A temporary group of agents working together to achieve a task.
- **Purpose:**
  - Tasks too complex for a single agent.
  - Efficiency gains through collaboration.
- **Characteristics:**
  - Agents bring complementary abilities/resources.
  - Coalitions disband after completing tasks.

---

## Key Issues in Coalition Formation
1. **Task and Coalition Selection:**
   - Which coalitions should an agent attempt to form?
   - How are tasks allocated among coalitions?
2. **Mechanism Design:**
   - Centralized (simpler but computationally expensive) vs. decentralized (complex, dynamic).
   - Benevolent vs. self-interested agents.
3. **Efficiency and Pay-off:**
   - Ensuring fairness and effectiveness in task distribution and reward sharing.

---

## Types of Coalition Formation
### **External Coalition Formation**
- Imposed by an external agency (e.g., central controller).
- Agents advertise capabilities and costs; the agency computes optimal coalitions.

### **Internal Coalition Formation**
- Achieved through self-organization among agents.
- Involves negotiation, task identification, and dynamic coalition generation.

---

## Coalition Formation Activities
1. **Coalition Value Calculation:** Assess benefits for each task-coalition pair.
2. **Coalition Structure Generation:** Partition agents into disjoint or overlapping coalitions.
3. **Pay-Off Distribution:** Allocate rewards based on contribution, roles, or outputs.

---

## Task Allocation Algorithm

### Goal
The primary objective of the task allocation algorithm is to efficiently distribute a set of tasks among coalitions of agents, ensuring that the allocation is both effective and optimal according to predefined criteria (e.g., minimal coordination cost, maximum benefit, or balanced workload distribution).

### Steps in the Task Allocation Algorithm

#### 1. Preliminary Stage
- **Coalition Identification:** Each agent begins by identifying potential coalitions it can join. This involves considering all possible subsets of agents that include the agent itself, with a limit on the maximum coalition size \(k\) (to control complexity).
- **Capabilities Exchange:** Agents communicate with each other to gather information about capabilities and potential coalition benefits.
- **Distributed Assignment of Responsibilities:** Each agent determines the specific coalitions for which it will calculate the value, ensuring an even distribution of workload across all agents.

#### 2. Iterative Stage
- **Value Calculation:** For each potential coalition-task pair, agents calculate the coalition's value. This involves assessing:
  - **Capabilities Match:** Whether the coalition's combined capabilities meet the task's requirements.
  - **Net Benefit:** The benefit of completing the task minus the costs of capabilities and internal coordination.
- **Coalition Formation:** The coalition with the highest value for a given task is selected.
  - Agents in the selected coalition execute the task.
  - These agents are removed from further coalition formation processes, and the completed task is removed from the task pool.
- **Recalculation and Update:** The algorithm iteratively recalculates the values of coalitions and assigns tasks until no tasks remain or resources are exhausted.

### Heuristics
- **Small Coalitions Preferred:** To minimize communication and coordination costs, smaller coalitions are favored.
- **Capability Optimization:** Coalitions are chosen to match task requirements as closely as possible, avoiding unnecessary overhead.

### Overlapping Coalitions
- In some cases, agents may belong to multiple coalitions if their resources allow. This introduces additional complexity:
  - **Dynamic Capability Updates:** After completing a task, an agent's remaining resources are recalculated to ensure accurate capability assessments for future coalitions.

### Challenges
- **Message Overhead:** High communication requirements in decentralized systems.
- **Redundancy:** Multiple agents might redundantly evaluate the same coalitions.
- **Memory Constraints:** Storing all potential coalitions requires significant resources.
- **Suboptimality:** Heuristic-based decisions may leave some tasks unassigned or result in non-optimal allocations.

### Example Execution
1. **Initial Calculations:** An agent \(A_1\) identifies potential coalitions such as \(\{A_1, A_2\}\), \(\{A_1, A_3\}\), and \(\{A_1, A_2, A_3\}\).
2. **Value Assignment:** The coalition \(\{A_1, A_2\}\) is found to have the highest value for task \(T_1\). This coalition executes \(T_1\).
3. **Recalculation:** Remaining coalitions are updated, and tasks \(T_2, T_3\), etc., are assigned in subsequent iterations.



## Improved Task Allocation Algorithm

This improved algorithm emphasizes a decentralized approach, aiming to balance computational load, reduce communication overhead, and ensure efficient task allocation.

### Steps in the Improved Algorithm

#### 1. Initial Distribution of Coalition Responsibilities
- **Local Assignment:** Each agent calculates the coalitions it could potentially participate in. This set is represented as \( P_i \), containing all possible coalitions with up to \( k \) members that include the agent itself.
- **Responsibility Assignment:** Agents collectively distribute coalition evaluation tasks. Each agent maintains a list \( L_i \), containing the coalitions it is responsible for evaluating.

#### 2. Iterative Coalition Formation
- **Stage 2a: Calculate Coalition Values**
  - For each coalition \( C \) in \( L_i \):
    1. Calculate the combined capability vector \( B_C \) as the sum of capabilities of all agents in \( C \).
    2. Check pending tasks \( t_j \):
       - Verify if \( C \) can complete \( t_j \) (\( B_C \geq B_{t_j} \)).
       - Compute the net benefit \( e_j \) as:
         \[
         e_j = \text{market value of required capabilities} - \text{capability costs} - \text{coordination costs}
         \]
       - Store the result \( (t_j, e_j) \) in a benefit set \( E_C \).
  - Identify the task \( t_{j,\text{best}} \) with the highest net benefit for \( C \) and calculate:
    - Coalition value \( V_C \).
    - Coalition cost \( c_C = 1 / V_C \).

- **Stage 2b: Form a Coalition**
  - **Select Optimal Coalition:** Each agent identifies the coalition in \( L_i \) with the lowest weight \( w_p = c_p / |C_p| \).
  - **Global Announcement:** Agents publicly share the weights of their optimal coalitions. The coalition \( C_{\text{low}} \) with the lowest global weight is selected to execute \( t_{\text{low},\text{best}} \).
  - **Update State:**
    - Agents in \( C_{\text{low}} \) execute the task, and their capabilities are updated to reflect resource usage.
    - Remove completed task \( t_{\text{low},\text{best}} \) from the task pool.
    - Recalculate coalition values for coalitions involving members of \( C_{\text{low}} \).

#### 3. Repeating the Process
- The process repeats until:
  - All tasks are assigned, or
  - No remaining coalitions can perform any tasks.

### Benefits of the Improved Algorithm
- **Balanced Distribution:** Responsibilities for coalition evaluation are evenly distributed among agents, avoiding bottlenecks.
- **Efficiency:** By focusing only on relevant coalitions, computational and communication costs are reduced.
- **Dynamic Adaptation:** Agents dynamically recalculate coalition values, accommodating changes in capabilities and task requirements.

### Example Execution
1. **Initial Stage:** Agent \( A_1 \) identifies potential coalitions \( \{A_1, A_2\}, \{A_1, A_4\}, \{A_1, A_2, A_4\}, \{A_1, A_2, A_3, A_4\} \).
2. **Coalition Evaluation:** Each coalition's capability and cost are calculated. For instance, coalition \( \{A_1, A_2, A_4\} \) may have the best value for task \( T_3 \).
3. **Task Execution:** Coalition \( \{A_1, A_2, A_4\} \) is formed to execute \( T_3 \). Afterward, the coalition disbands, and its agents update their states for the next round of task allocation.

This improved algorithm ensures a scalable, decentralized solution for task allocation in multi-agent systems.


### Example: RETSINA Framework
- **Task Assignment:**
  - Tasks are decomposed into subtasks by a central Task Agent.
  - A Middle Agent facilitates coalition formation by matching agents to subtasks.
- **Dynamic Updates:**
  - After completing subtasks, agents report changes in their capabilities to update coalition options dynamically.

This systematic approach ensures that tasks are allocated efficiently while addressing the inherent complexity of coalition formation in multi-agent systems.


---

## Suggested Readings
1. Shehory, Kraus: *Methods for task allocation via agent coalition formation*.
2. Rahwan, Michalak, Wooldridge, Jennings: *Coalition structure generation: a survey* (2015).
3. M. Wooldridge: *An Introduction to MultiAgent Systems* (Chapter 13).
4. Rahwan: *Algorithms for coalition formation in MAS* (PhD thesis, 2007).

---

# Lecture 7: Cooperation in MAS (III) – Negotiation via Auctions

## Overview
This lecture explores auctions as a negotiation mechanism for resource allocation and conflict resolution in Multi-Agent Systems (MAS). It details various auction formats, processes, and their applications in competitive environments.

---

## Negotiation in MAS
- **Need for Negotiation:**
  - Conflicting goals and limited resources necessitate compromises and agreements.
- **Negotiation Protocols:**
  - Govern agent interactions with private (agent strategies) and public elements (negotiation sets and protocol rules).
  - Rules include:
    - Admission, interaction, and validity rules.
    - Outcome determination for reaching agreements.

---

## Auctions as Negotiation Mechanisms
- **Definition:** Auctions allocate goods/resources through competitive bidding among self-interested parties.
- **Applications:**
  - Telecommunications, mining rights, advertising slots (e.g., Google AdSense), collectibles, and agricultural products.

### **Advantages of Auctions**
- Create competition and flexibility.
- Faster and less costly than direct negotiations.

---

## Auction Participants and Concepts
- **Auctioneer:** Organizes the auction, aiming for the highest (selling) or lowest (buying) price.
- **Bidders:** Buyers or sellers competing to achieve their goals.

### **Key Concepts:**
- **Bid:** Offer to buy or sell.
- **Reservation Price:** Maximum or minimum price acceptable to a buyer or seller (usually private).
- **Clearing Price:** Final transaction price.

---

## Auction Formats
### **Basic Types**
1. **English Auction:**
   - Open-outcry, ascending-price format.
   - Bidders raise bids; the highest bidder wins.
   - **Disadvantages:** Risk of overbidding, phantom bids, and collusion.

2. **Dutch Auction:**
   - Open, descending-price format.
   - The first bidder to accept the price wins.
   - **Advantages:** Efficient for real-time goods (e.g., fresh produce).

3. **First-Price Sealed-Bid Auction:**
   - Bids are submitted privately.
   - The highest bidder wins and pays their bid amount.
   - **Strategy:** Bid below true valuation to maximize profit.

4. **Vickrey Auction (Second-Price Sealed-Bid):**
   - The highest bidder wins but pays the second-highest bid.
   - **Advantages:** Encourages truthful bidding and avoids counter-speculation.

---

## Advanced Auction Types
1. **Multi-Unit Auctions:**
   - Allocate multiple identical units.
   - Bids are ranked, and items are awarded until supply is exhausted.

2. **Multi-Attribute Auctions:**
   - Bids include multiple attributes (e.g., price, delivery time, quality).
   - Common in procurement scenarios.
   - Evaluated using scoring functions for weighted attributes.

3. **Combinatorial Auctions:**
   - Bids for bundles of items, considering complementarity and substitutability.
   - **Challenges:** Winner determination and managing interdependencies.
   - **Advantages:** Flexible and efficient allocation of resources.

---

## Challenges and Disadvantages
1. **Winner’s Curse:**
   - Overestimation of value leads to losses for winning bidders.
   - **Mitigation:** Rational bidding and strategic information use.

2. **Lying Auctioneer:**
   - Manipulates bids or reservation prices, especially in sealed-bid auctions.
   - **Solution:** Cryptographic signatures.

3. **Sniping:**
   - Late bids to prevent competition in online auctions.
   - Avoids price escalation and preference revelation.

---

## Proposed Readings
- Chapter 8: *Agent Technology for E-Commerce* by M. Fasli.
- Chapter 14: *An Introduction to MultiAgent Systems* by M. Wooldridge (2nd edition).

---

# Lecture 8: Cooperation in MAS (IV) – Voting Protocols

## Overview
This lecture explores voting as a distributed decision-making mechanism in Multi-Agent Systems (MAS). It covers social choice rules, simple and complex voting mechanisms, and their strengths and limitations.

---

## Voting in MAS
- **Definition:** A negotiation mechanism to decide outcomes based on inputs (votes) from agents for competing options.
- **Assumption:** Voters are truthful in expressing preferences (though insincere voting can occur for strategic reasons).

---

## Elements of Voting Protocols
1. **Agents (A):** The voters.
2. **Alternatives (O):** The options to be ranked.
3. **Preference Relations:** Individual agent preferences for alternatives (weak or linear orders).

---

## Social Choice Rules
- **Input:** Agents' preferences.
- **Output:** Aggregated social preference ordering (<*) of alternatives.
- **Desirable Properties:**
  - **Calculability:** Defined for all inputs.
  - **Completeness:** Every pair of alternatives is comparable.
  - **Linearity:** Preferences are antisymmetric and transitive.
  - **Anonymity/No Dictatorship:** Outcome depends on preferences, not agents.
  - **Pareto Efficiency:** If all agents prefer A over B, A is preferred.
  - **Neutrality:** Unaffected by naming or order of alternatives.
  - **Independence of Irrelevant Alternatives:** Adding/removing irrelevant alternatives does not affect outcomes.

**Arrow’s Impossibility Theorem:** No rule satisfies all these properties; trade-offs are necessary.

---

## Simple Voting Mechanisms
1. **Plurality Voting:**
   - Each agent votes for one alternative.
   - Winner: Most votes.
   - **Problems:**
     - "Useful vote" effect.
     - Influence of irrelevant alternatives.
     - Majority dissatisfaction (e.g., 58% may consider the winner the worst option).

2. **Anti-Plurality Voting:**
   - Each agent casts a negative vote for their least preferred alternative.
   - Winner: Fewest negative votes.
   - **Drawback:** May select an option that is no one's top preference.

3. **Best-Worst Voting:**
   - Agents vote for their top and bottom choices.
   - **Scoring:** Positive points for top choice, negative for bottom.
   - Winner: Highest total points.

4. **Approval Voting:**
   - Agents vote for all acceptable options.
   - **Variant:** k-approval voting limits the number of choices per agent.

---

## Protocols Based on Linear Orders
1. **Binary Voting:**
   - Sequential pairwise comparisons.
   - Winner: Last option remaining.
   - **Problems:** Outcome depends on pairing order; violates neutrality.

2. **Borda Voting:**
   - Assigns points based on rank order.
   - Winner: Highest total score.
   - **Drawbacks:** Sensitive to irrelevant alternatives; computationally expensive.

3. **Condorcet Voting:**
   - Pairwise comparisons for all candidates.
   - Winner: Option preferred over all others.
   - **Problem:** May result in circular ambiguities.

---

## Complex Voting Mechanisms
### **Linguistic Information:**
- Uses linguistic labels (e.g., "Poor" to "Excellent") for evaluations.
- Aggregates voter opinions into a collective evaluation using distance measures.

### **Uncertain Opinions:**
- Voter preferences represented as intervals over linguistic labels.
- Aggregated as intervals minimizing distance to individual opinions.

---

## Challenges and Trade-offs
1. **Insincere Voting:** Strategic misrepresentation of preferences.
2. **Computational Complexity:** Some protocols, like Borda, require significant resources.
3. **Influence of Protocols:** Outcomes vary significantly with protocol choice.
4. **Arrow’s Theorem:** Highlights inherent trade-offs in social choice rules.

---

## Suggested Readings
1. Chapter 12: *An Introduction to Multi-Agent Systems* by M. Wooldridge (2nd edition).
2. Chapter 9: *Agent Technology for E-Commerce* by M. Fasli.

---

# Lecture 9: Cooperation in MAS (V) – Implicit Methods

## Overview
This lecture explores implicit cooperation methods in Multi-Agent Systems (MAS), focusing on indirect cooperation, reasoning mechanisms, and societal approaches such as electronic institutions and organizational structures.

---

## Implicit Cooperation
- **Definition:** Agents achieve socially coordinated behavior to solve global problems without explicit communication.
- **Motivations:**
  - **Speed:** Communication delays can lead to missed opportunities (e.g., dynamic environments like sports).
  - **Security:** Concealing plans or strategies.
  - **Complexity:** Some agents lack the sophistication to process complex plans.
  - **Lack of Communication Channels:** Physical or network limitations.

---

## Options for Implicit Cooperation
### 1. **Indirect Cooperation**
- **Characteristics:**
  - No communication or pre-defined rules.
  - Agents act independently but produce coherent global behavior.
- **Example:** Network routing via ant algorithms:
  - Agents (ants) leave pheromones on paths to indicate routes.
  - Pheromone levels guide others, degrading over time to reflect dynamic updates.

### 2. **Reasoning Mechanisms**
#### A. **Agent Modeling:**
- Recursive modeling to deduce beliefs, desires, and intentions from observed actions.
- **Plan Recognition:** Analyze activities to infer goals.
- **Game Playing:** Use strategies like minimax for opponent modeling.

#### B. **Societal Modeling:**
- **Social Laws:** Global rules that govern behavior (e.g., "drive on the right").
- **Electronic Institutions:** Formal frameworks with norms, protocols, and conventions.
- **Organizational Structures:** Define relationships and roles to guide interactions.

---

## Electronic Institutions (e-Institutions)
- **Definition:** Computational models of social structures that enforce norms and protocols.
- **Key Features:**
  - Reduce uncertainty and simplify decision-making.
  - Ensure adherence to norms through middleware like AMELI, which mediates agent communication and controls scene transitions.
- **Components:**
  - Dialogical Framework: Defines roles and communication protocols.
  - Performative Structure: Specifies allowable scenes and transitions.
  - Norms: Guide acceptable behaviors and commitments.

---

## Organizational Structures
- **Purpose:** Define patterns of relationships and control to streamline coordination.
- **Types of Structures:**
  1. **Markets:** Focus on exchanges of goods and services (e.g., negotiation-based interactions).
  2. **Networks:** Emphasize dynamic collaboration with contracts and mutual interests.
  3. **Hierarchies:** Use command and control for efficiency in production or specialized tasks.
  ![Social Structures](figures/Social%20Structures.png)

### **Examples of Organizational Structures**
1. **Product Hierarchy:**
   - Separate teams for each product.
   - Easy coordination within teams but risks inefficiencies from task duplication.
2. **Functional Hierarchy:**
   - Specialization by task (e.g., design, engineering).
   - Encourages resource sharing but centralizes workload on managers.
3. **Product + Functional Hierarchy:**
   - Combines both approaches for balanced coordination.
   - Managers act as brokers for shared resources and task delegation.
4. **Flat Structure:**
   - Direct communication between product managers and agents.
   - Can lead to inefficiencies and difficulty managing global behavior.

---

## Social Abstractions
- **Roles:** Define activities/services for achieving societal goals, abstracting from specific individuals.
- **Role Dependencies:** Establish relationships between roles to facilitate cooperation and task delegation.

---

## Applications and Critiques
- **Applications:**
  - Useful for streamlining distributed problem-solving in MAS.
  - Focus on structures that align with environmental needs (e.g., peer systems, markets).
- **Critiques:**
  - Over-reliance on centralized control undermines MAS benefits like reliability and concurrency.
  - Assumes at least one agent has a global overview, which may be unrealistic.

---

## Suggested Readings
- Sections 8.6.3/4: *An Introduction to MultiAgent Systems* by M. Wooldridge (2nd edition).
- Additional papers available on the URV Virtual Campus.

---

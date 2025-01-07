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

---

## Partial Global Planning (PGP)
### **Overview**
- Developed by Durfee & Lesser for Distributed Vehicle Monitoring (DVM).
- Integrates planning and execution in inherently distributed tasks.

### **Phases**
1. **Create Local Plans:**
   - Each agent generates a sequence of actions for assigned tasks.
   - Plans are modifiable and account for action duration and quality.
2. **Exchange Local Plans:**
   - Agents share relevant plans with others based on system structure.
3. **Generate Partial Global Plans:**
   - Combine local plans into a global activity map.
   - Identify sub-goals and opportunities for better coordination.
4. **Optimize Partial Global Plans:**
   - Reorder tasks, reallocate work, and adjust plans based on authority or redundancy.

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

### **Agent Structure**
1. **Belief Database:** Stores task structure information.
2. **Coordination Mechanisms:** Analyze task relationships and impose constraints.
3. **Local Scheduler:** Builds schedules considering commitments and constraints.

### **Coordination Mechanisms**
1. **Update Non-Local Viewpoints:** Share task information between agents.
2. **Manage Hard Coordination Relationships:** Ensure timely task execution to avoid bottlenecks.
3. **Manage Soft Coordination Relationships:** Optimize for quality and speed when possible.
4. **Detect Redundancy:** Resolve duplicate efforts by assigning tasks to the most suitable agent.

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

## Task Allocation via Coalition Formation
- **Goal:** Efficiently distribute tasks among agent subgroups.
- **Optimization Criteria:**
  - Minimize coalition size or number.
  - Match task requirements to coalition capabilities.
  - Maximize overall benefit.

---

## Simplified Assumptions
- Agents can only belong to one coalition at a time.
- Coalitions work on a single task at a time.
- Coalition capabilities are the sum of member capabilities.

---

## Task Allocation Algorithm
1. **Preliminary Stage:**
   - Agents calculate potential coalitions they can participate in.
2. **Iterative Stage:**
   - Assign tasks to the best coalition based on calculated values.
   - Form a coalition, execute the task, and remove it from the pool.
   - Repeat until all tasks are assigned or agents/resources are exhausted.

### **Heuristics**
- Prefer smaller coalitions to reduce coordination costs.
- Limit coalition size to manage complexity.

---

## Overlapping Coalitions
- Agents can participate in multiple coalitions if resources allow.
- Requires updating capabilities dynamically after each task execution.

---

## Example: RETSINA Framework
- **Task Assignment:**
  - Tasks decomposed into subtasks by a Task Agent.
  - Middle Agents identify potential coalitions for each subtask.
- **Coalition Formation:**
  - Coalitions with the highest value are selected to execute subtasks.
- **Dynamic Updates:**
  - Agents report changes in capabilities to update future coalition options.

---

## Challenges and Drawbacks
- **Message Overhead:** High communication costs in decentralized systems.
- **Redundancy:** Duplicate coalition evaluations by different agents.
- **Memory Requirements:** Storing large sets of potential coalitions.
- **Suboptimality:** Tasks may remain unassigned due to heuristic limitations.

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

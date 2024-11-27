> [Lect 8 - Cooperation 4 - Voting protocols, p.5](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=5&selection=4,0,8,27)
> Self-interested agents can benefit from insincerely declaring their preferences

> ([Lect 8 - Cooperation 4 - Voting protocols, p.9](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=9&selection=4,0,21,48))
> ### Social choice rule: Desirable properites
> - Calculability A social preference ordering <* should exist for all possible inputs 
> - Completeness <* should be defined for every pair of alternatives (o, o') ∈ O
> - Linearity <* should be antisymmetric and transitive over O
> 
> ([Lect 8 - Cooperation 4 - Voting protocols, p.10](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=10&selection=4,0,7,15))
> Anonymity / No dictatorship The outcome of the social choice rule depends on the set of opinions, but not on which agents have these opinions.

> ([Lect 8 - Cooperation 4 - Voting protocols, p.11](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=11&selection=4,0,14,48))
> Unanimity / Pareto efficiency If ∀i ∈A (o <i o8), then (o <* o8) Do not misorder the options if all agents agree. If everybody thinks that A is better than B, A should be preferred to B in the aggregated order

> ([Lect 8 - Cooperation 4 - Voting protocols, p.12](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=12&selection=2,0,12,40))
> - Neutrality The outcome of the social choice rule should not depend on how alternatives are named or ordered
> - Independence of irrelevant alternatives Removing / Adding an irrelevant alternative should not affect the winner of the vote

> ([Lect 8 - Cooperation 4 - Voting protocols, p.16](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=16&selection=8,0,30,33))
> Plurality voting -> **Useful vote**
> - Quite common effect of political polls
> - 45 % option A, 40% option B, 15% option C
> - The most socially preferred option is A => it should be the winner if all agents vote truthfully 
> - The agents that prefer option C know that they have no possibility to win, and most of them (80%) prefer option B to option A => 80% vote for B and 20% for A
> - A: 48% B: 52%, and B finally wins

> ([Lect 8 - Cooperation 4 - Voting protocols, p.21](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=21&selection=0,0,0,33))
> **Plurality voting: Anti-Plurality**
>
> ([Lect 8 - Cooperation 4 - Voting protocols, p.21](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=21&selection=17,0,21,37))
> Last: C (40% negative votes) – but also first option for 60% A and B get 30% negative votes D is the winner with 0 negative votes – but it was not the first or second option for anyone

> ([Lect 8 - Cooperation 4 - Voting protocols, p.23](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=23&selection=0,0,0,17))
> **Best-worst voting**

> ([Lect 8 - Cooperation 4 - Voting protocols, p.24](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=24&selection=0,0,0,15))
> Approval voting

> ([Lect 8 - Cooperation 4 - Voting protocols, p.25](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=25&selection=0,0,0,32))
> Protocols based on linear orders

## Binary voting: the ordering problem

> ([Lect 8 - Cooperation 4 - Voting protocols, p.27](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=27&selection=33,0,41,45))
> The order of the pairings affects the outcome!
> - The voter organiser may influence the result
> - The last options have more chances of winning

> ([Lect 8 - Cooperation 4 - Voting protocols, p.31](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=31&selection=0,0,0,12))
> Borda voting

## Generalizing voting protocols
> ([Lect 8 - Cooperation 4 - Voting protocols, p.40](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=40&selection=4,0,56,31))
> - Scoring vector
> 	- S = (s1, …, sn) with si >= si+1 and s1 > sn
> - Each voter gives si points to his i-th option
> - The option with more points wins
> - Examples with 4 options
> 	- vector (4,3,2,1) => Borda protocol
> 	- vector (1,0,0,0) => Plurality protocol
> 	- vector (0,0,0,-1) => Anti-plurality protocol
> 	- vector (1,0,0,-1) => Best-worst MESIIA / MAI – Multi-Agent Systems Cooperation in MAS (IV)

![Lect 8 - Cooperation 4 - Voting protocols, p.41](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=41&rect=72,49,653,447)

## Linguistic information: uncertain preferences
> ([Lect 8 - Cooperation 4 - Voting protocols, p.50](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=50&selection=5,0,7,32))
> Each voter represents the opinion on every alternative with an interval defined over an ordered set of linguistic labels

![Lect 8 - Cooperation 4 - Voting protocols, p.50](Lect%208%20-%20Cooperation%204%20-%20Voting%20protocols.pdf#page=50&rect=132,186,585,298)

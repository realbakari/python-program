The King wants to marry off his daughter, and he wants her husband to have the greatest innate luckiness possible. To find such a person he decided to hold a heads-or-tails tournament.

If person 𝐴 with luckiness 𝑥 and person 𝐵 with luckiness 𝑦 play heads-or-tails against each other, person 𝐴 wins with probability 𝑥/(𝑥+𝑦).

The tournament has several rounds. Each round some participants are split into pairs. Each pair plays against each other, and the loser leaves the tournament.

The participants are numbered from 1 to 𝑛. During the first round, a number 𝑘 (1≤𝑘≤𝑛) is selected such that 𝑛−𝑘/2 is a power of 2 (such 𝑘 always exists and is unique). Only participants numbered from 1 to 𝑘 take part in the first round. It ensures that in all other rounds the number of participants is the power of 2.

During other rounds, all the participants who still have not left the tournament take part. If during some round, participants numbered 𝑝1<…<𝑝2𝑚 take part, then they are split into pairs in the following manner: participant 𝑝2𝑖−1 plays against participant 𝑝2𝑖 for each 𝑖 from 1 to 𝑚.

The rounds are held until only one participant is left. He is declared the winner of the tournament and he will marry the King's daughter. The princess can't wait to find out who is her future husband. She asked every participant to tell her his luckiness. Assuming they did not lie, she wants to know the probability of each participant winning the tournament. As you are the best friend of the princess, she asks you to help her.

Input
The first line of the input contains the number of participants, 𝑛 (2≤𝑛≤3⋅105). The second line of the input contains 𝑛 integer numbers, 𝑎1,…,𝑎𝑛 (1≤𝑎𝑖≤109). The luckiness of the 𝑖-th participant equals to 𝑎𝑖.

Output
Print 𝑛 numbers 𝑝𝑖. The 𝑖-th number should be the probability of the 𝑖-th participant winning the tournament. The absolute error of your answer must not exceed 10−9.

Example
```
input
5
1 4 1 1 4
```
```
output
0.026 0.3584 0.0676 0.0616 0.4864
```
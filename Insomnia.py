"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/148/A ----------------

«One dragon. Two dragon. Three dragon», — the princess was counting. 
She had trouble falling asleep, and she got bored of counting lambs when she was nine.

However, just counting dragons was boring as well, so she entertained herself at best she could. 
Tonight she imagined that all dragons were here to steal her, and she was fighting them off. 
Every k-th dragon got punched in the face with a frying pan. Every l-th dragon got his tail shut 
into the balcony door. Every m-th dragon got his paws trampled with sharp heels. 
Finally, she threatened every n-th dragon to call her mom, and he withdrew in panic.

How many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?

Input
Input data contains integer numbers k, l, m, n and d, each number in a separate line 
(1 ≤ k, l, m, n ≤ 10, 1 ≤ d ≤ 10^5).

Output
Output the number of damaged dragons.

Input:
1
2
3
4
12
Output:
12
"""
k = int(input())
l = int(input())
m = int(input()) 
n = int(input()) 
d = int(input()) + 1
limits = [k, l, m, n]
exclusions = 0
damaged = 0
for i in range(1, d):
    excluded = False  # assume that the number is not excluded by default
    for j in range(len(limits)):  # loop through the four limits
        if i % limits[j] == 0:  # check if the number meets the current limit
            excluded = True
            damaged += 1# if it does, mark it as excluded
            break  # exit the inner loop early, since the number is already excluded
    if not excluded:  # if the number was not excluded by any of the limits
       exclusions += 1  # add it to the list of excluded numbers
print(damaged)
        
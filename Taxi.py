"""
-------- Link for the challenge: https://codeforces.com/contest/158/problem/B ---------

After the lessons n groups of schoolchildren went outside and decided to visit Polycarpus to
celebrate his birthday. We know that the i-th group consists of si friends (1 ≤ s(i) ≤ 4),
and they want to go to Polycarpus together. They decided to get there by taxi.
Each car can carry at most four passengers. What minimum number of cars will the children need if all
members of each group should ride in the same taxi (but one taxi can take more than one group)?

Input
The first line contains integer n (1 ≤ n ≤ 10^5) — the number of groups of schoolchildren.
The second line contains a sequence of integers s1, s2, ..., sn (1 ≤ s(i) ≤ 4). 
The integers are separated by a space, s(i) is the number of children in the i-th group.

Output
Print the single number — the minimum number of taxis necessary to drive all children to Polycarpus.

Input:
5
1 2 4 3 3

Output:
4

"""

import math
groups = int(input())
values = list(map(int, input().split()))
numberOfFours = values.count(4)
numberOfThrees = values.count(3)
numberOfTwos = values.count(2)
numberOfOnes = values.count(1)
ans = numberOfFours
while(numberOfThrees > 0 and numberOfOnes > 0):
    numberOfThrees -= 1
    numberOfOnes -= 1
    ans += 1
while(numberOfTwos > 0 and numberOfOnes > 0):
    numberOfTwos -= 1
    if(numberOfOnes >= 2):
        numberOfOnes -= 2
    else:
        numberOfOnes -= 1
    ans += 1
temp = math.ceil(numberOfTwos / 2)
ans += temp
if(numberOfThrees > 0):
    ans += numberOfThrees
while(numberOfOnes > 0):
    numberOfOnes -= 4
    ans += 1
   
print(ans)
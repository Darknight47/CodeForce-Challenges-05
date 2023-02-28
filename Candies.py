"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/306/A -----------

Polycarpus has got n candies and m friends (n ≥ m).
He wants to make a New Year present with candies to each friend.
Polycarpus is planning to present all candies and he wants to do this in the fairest (that is, most equal) manner.
He wants to choose such ai, where ai is the number of candies in the i-th friend's present,
that the maximum ai differs from the least ai as little as possible.

For example, if n is divisible by m, then he is going to present the same number of candies
to all his friends, that is, the maximum ai won't differ from the minimum one.

Input
The single line of the input contains a pair of space-separated positive integers n, m
(1 ≤ n, m ≤ 100;n ≥ m) — the number of candies and the number of Polycarpus's friends.

Output
Print the required sequence a1, a2, ..., am, where ai is the number of candies in the i-th
friend's present. All numbers ai must be positive integers, total up to n, the maximum one
should differ from the minimum one by the smallest possible value.

Input:
12 3

Output:
4 4 4

"""
import math
n, m = map(int, input().split())
div = math.floor(n / m)
arr = [div] * m
temp = div * m
diff = n - temp
for i in range(len(arr)):
    diff -= 1
    if(diff < 0):
        break
    arr[i] += 1
arr.sort()
print(*arr)
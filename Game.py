"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/673/A -----------

Bear Limak likes watching sports on TV. He is going to watch a game today. The game lasts 90 minutes and there are no breaks.

Each minute can be either interesting or boring. If 15 consecutive minutes are boring then Limak immediately turns TV off.

You know that there will be n interesting minutes t1, t2, ..., tn. Your task is to calculate for how many minutes Limak will watch the game.

Input
The first line of the input contains one integer n (1 ≤ n ≤ 90) — the number of interesting minutes.

The second line contains n integers t1, t2, ..., tn (1 ≤ t1 < t2 < ... tn ≤ 90), given in the increasing order.

Output
Print the number of minutes Limak will watch the game.

Input:
3
7 20 88

Output:
35
"""
interestingsMin = int(input())
lst = list(map(int, input().split()))
first = 0
ans = 90
for i in range(interestingsMin):
    temp = lst[i]
    diff = temp - first
    if(diff > 15):
        ans = first + 15
        break
    else:
        first = temp
t = ans - first
if(t > 15):
    ans = first + 15
print(ans)
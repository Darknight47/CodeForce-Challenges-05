"""
------- Link for the challenge: https://codeforces.com/contest/1742/problem/B -------

You are given an array a of n positive integers. Determine if, by rearranging the elements, 
you can make the array strictly increasing. In other words, determine if it is possible 
to rearrange the elements such that a1<a2<⋯<an holds.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the length of the array.

The second line of each test case contains n integers a(i) (1 ≤ a(i) ≤ 10^9) — the elements of the array.

Output
For each test case, output "YES" (without quotes) if the array satisfies the condition, and "NO" (without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    tempSet = set(map(int, input().split()))
    if(len(tempSet) == 1 and sze > 1):
        print("NO")
    elif(len(tempSet) < sze):
        print("NO")
    else:
        print("YES")
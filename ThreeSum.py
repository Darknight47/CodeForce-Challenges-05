"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/1742/A ---------

You are given three integers a, b, and c. 
Determine if one of them is the sum of the other two.

Input
The first line contains a single integer t (1 ≤ t ≤ 9261) — the number of test cases.

The description of each test case consists of three integers a, b, c(0 ≤ a,b,c ≤ 20).

Output
For each test case, output "YES" if one of the numbers is the sum of the other two, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
"""
cases = int(input())
for i in range(cases):
    a, b, c = map(int, input().split())
    ok = False
    t1 = a + b
    t2 = a + c
    t3 = b + c
    if(t1 == c):
        ok = True
    elif(t2 == b):
        ok = True
    elif(t3 == a):
        ok = True
    print("YES" if ok else "NO")
    
"""
-------------- Link for the challenge: https://codeforces.com/problemset/problem/1584/A -------------

Ivan decided to prepare for the test on solving integer equations. 
He noticed that all tasks in the test have the following form:

You are given two positive integers u and v, find any pair of integers 
(not necessarily positive) x, y, such that
    x/u + y/v= x+y / u+v.
The solution x = 0, y = 0 is forbidden, so you should find any solution with (x,y)≠(0,0).
Please help Ivan to solve some equations of this form.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases. 
The next lines contain descriptions of test cases.

The only line of each test case contains two integers u and v (1 ≤ u , v ≤ 10^9 ) — the parameters of the equation.

Output
For each test case print two integers x , y — a possible solution to the equation. 
It should be satisfied that −10^18 ≤ x,y ≤ 10^18 and (x,y)≠(0,0).

We can show that an answer always exists. If there are multiple possible solutions you can print any.

Input:
4
1 1
2 3
3 5
6 9

Output:
-1 1
-4 9
-18 50
-4 9

"""

cases = int(input())
for i in range(cases):
        x, y = map(int, input().split())
        print((x*x * -1), (y*y))
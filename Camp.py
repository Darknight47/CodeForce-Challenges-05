"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/672/A --------------

Every year, hundreds of people come to summer camps, they learn new algorithms and solve hard problems.

This is your first year at summer camp, and you are asked to solve the following problem. 
All integers starting with 1 are written in one line. The prefix of these line is "123456789101112131415...". 
Your task is to print the n-th digit of this string (digits are numbered starting with 1.

Input
The only line of the input contains a single integer n (1 ≤ n ≤ 1000) — the position of the digit you need to print.

Output
Print the n-th digit of the line.

Input:
11
Output:
0
"""
pos = int(input())
if(pos < 10):
    print(pos)
else:
    sze = 9
    tempNum = 9
    founded = False
    while True:
        tempNum += 1
        s = str(tempNum)
        for ch in s:
            sze += 1
            if(sze == pos):
                print(ch)
                founded = True
                break
        if(founded):
            break
            
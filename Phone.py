"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/1060/A ---------

Let's call a string a phone number if it has length 11 and fits the pattern "8xxxxxxxxxx", 
where each "x" is replaced by a digit.

For example, "80123456789" and "80000000000" are phone numbers, while "8012345678" and "79000000000" are not.

You have n cards with digits, and you want to use them to make as many phone numbers as possible. 
Each card must be used in at most one phone number, and you don't have to use all cards. 
The phone numbers do not necessarily have to be distinct.

Input
The first line contains an integer n — the number of cards with digits that you have (1 ≤ n ≤ 100).

The second line contains a string of n digits (characters "0", "1", ..., "9") s1,s2,…,sn. 
The string will not contain any other characters, such as leading or trailing spaces.

Output
If at least one phone number can be made from these cards, output the maximum number 
of phone numbers that can be made. Otherwise, output 0.

Input:
11
00000000008
Output:
1
"""
import math
sze = int(input())
s = input()
ans = 0
eight = s.count("8")
if(sze == 11 and eight >= 1):
    ans = 1
elif(sze > 11):
    t = math.floor(sze / 11)
    if(eight <= 0):
        ans = 0
    elif(eight >= t):
        ans = t
    elif(eight < t):
        ans = eight
print(ans)
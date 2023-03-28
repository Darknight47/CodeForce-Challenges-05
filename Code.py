"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/172/A ---------

Polycarpus has n friends in Tarasov city. Polycarpus knows phone numbers of all his friends: 
they are strings s1, s2, ..., sn. All these strings consist only of digits and have the same length.

Once Polycarpus needed to figure out Tarasov city phone code. He assumed that the phone code of 
the city is the longest common prefix of all phone numbers of his friends. In other words, 
it is the longest string c which is a prefix (the beginning) of each si for all i (1 ≤ i ≤ n). 
Help Polycarpus determine the length of the city phone code.

Input
The first line of the input contains an integer n (2 ≤ n ≤ 3·10^4) — the number of Polycarpus's friends. 
The following n lines contain strings s1, s2, ..., sn — the phone numbers of Polycarpus's friends. 
It is guaranteed that all strings consist only of digits and have the same length from 1 to 20, inclusive. 
It is also guaranteed that all strings are different.

Output
Print the number of digits in the city phone code.

Input:
4
00209
00219
00999
00909

Output:
2
"""
cases = int(input())
lst = list(input())
l = len(lst)
maxPrefix = 40000
for i in range(cases - 1):
    tempLst = list(input())
    tempMax = 0
    for j in range(l):
       first = lst[j]
       second = tempLst[j]
       if(first == second):
           tempMax += 1
       else:
           break
    if(tempMax < maxPrefix):
        maxPrefix = tempMax
print(maxPrefix)    
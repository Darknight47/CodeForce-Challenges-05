"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/821/A ----------

Okabe needs to renovate the Future Gadget Laboratory after he tried 
doing some crazy experiments! The lab is represented as an n by n square grid of integers. 
A good lab is defined as a lab in which every number not equal to 1 can be expressed as the 
sum of a number in the same row and a number in the same column. In other words, 
for every x, y such that 1 ≤ x, y ≤ n and ax, y ≠ 1, there should exist two indices s and 
t so that ax, y = ax, s + at, y, where a(i), j denotes the integer in i-th row and j-th column.

Help Okabe determine whether a given lab is good!

Input
The first line of input contains the integer n (1 ≤ n ≤ 50) — the size of the lab.

The next n lines contain n space-separated integers denoting a row of the grid. 
The j-th integer in the i-th row is a(i), j (1 ≤ a(i), j ≤ 10^5).

Output
Print "Yes" if the given lab is good and "No" otherwise.

You can output each letter in upper or lower case.

Input:
3
1 1 2
2 3 1
6 4 1
Output:
YES

"""
n = int(input())
arr = []
for i in range(n):
    lstTemp = list(map(int, input().split()))
    arr.append(lstTemp)
ok = True
for z in range(n):
    lst = arr[z]
    for tNumIndxRow in range(n):
        numTemp = lst[tNumIndxRow]
        if(numTemp > 1):
            okTemp = False
            for tNumIndxSameRow in range(n):
                if(tNumIndxRow != tNumIndxSameRow):
                    tnr = lst[tNumIndxSameRow]
                    for tNumIndxCol in range(n):
                        if(z != tNumIndxCol):
                            tnc = arr[tNumIndxCol][tNumIndxRow]
                            tempAns = tnr + tnc
                            if(tempAns == numTemp):
                                okTemp = True
                                break
                if(okTemp == True):
                    break
            if(okTemp == False):
                ok = False
                break
    if(ok == False):
        break
print("YES" if ok else "NO")
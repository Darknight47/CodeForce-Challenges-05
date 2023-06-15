"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/1152/A --------------

On a random day, Neko found n treasure chests and m keys.
The i-th chest has an integer a(i) written on it and the j-th key has an integer b(j) on it.
Neko knows those chests contain the powerful mysterious green Grapes, thus Neko wants to open as many treasure chests as possible.

The j -th key can be used to unlock the i-th chest if and only if the sum of the key number and the chest number is an odd number.
Formally, ai+bj≡1(mod2). One key can be used to open at most one chest, and one chest can be opened at most once.

Find the maximum number of chests Neko can open.

Input:
The first line contains integers n and m (1 ≤ n,m ≤ 10^5) — the number of chests and the number of keys.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the numbers written on the treasure chests.

The third line contains m integers b1,b2,…,bm (1 ≤ b(i) ≤ 10^9) — the numbers written on the keys.

Output:
Print the maximum number of chests you can open.
"""
n, m = map(int, input().split())
chests = list(map(int, input().split()))
keys = list(map(int, input().split()))
ans = 0
evensChest = 0
oddsChest = 0
evensKey = 0
oddsKey = 0
for i in range(n):
    tempChest = chests[i]
    if(tempChest % 2 == 0):
        evensChest += 1
    else:
        oddsChest += 1
for j in range(m):
    tempKey = keys[j]
    if(tempKey % 2 == 0):
        evensKey += 1
    else:
        oddsKey += 1

temp1 = min(evensChest, oddsKey)
temp2 = min(oddsChest, evensKey)
ans = temp1 + temp2

print(ans) 
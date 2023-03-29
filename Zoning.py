"""
-------- Link for the challenge: https://codeforces.com/contest/1162/problem/A ----------------

You are planning to build housing on a street. There are n spots available on the street on which you 
can build a house. The spots are labeled from 1 to n from left to right. In each spot, you can build 
a house with an integer height between 0 and h.

In each spot, if a house has height a, you will gain a^2 dollars from it.

The city has m zoning restrictions. The i-th restriction says that the tallest 
house from spots l(i) to r(i) (inclusive) must be at most x(i).

You would like to build houses to maximize your profit. Determine the maximum profit possible.

Input
The first line contains three integers n, h, and m(1 ≤ n,h,m ≤ 50) — the number of spots, 
the maximum height, and the number of restrictions.

Each of the next mlines contains three integers l(i), r(i), and x(i) (1 ≤ l(i) ≤ r(i) ≤ n, 0 ≤ x(i) ≤ h) — 
left and right limits (inclusive) of the i-th restriction and the maximum possible height in that range.

Output
Print a single integer, the maximum profit you can make.

Input:
3 3 3
1 1 1
2 2 3
3 3 2

Output:
14
"""
spots, maxHeight, restrictions = map(int, input().split())
diction = {}
for i in range(restrictions):
    tv = input()
    tk = i + 1
    diction[tk] = tv
ans = 0
for j in range(spots):
    spotNum = j + 1
    tempFound = False
    tm = 100
    for z in diction.values():
        left, right, tempMax = map(int, z.split())
        if(spotNum >= left and spotNum <= right):
            if(tm > tempMax):
                tm = tempMax
            tempFound = True
    if(tempFound):
        ans += tm * tm
    else:
        ans += maxHeight * maxHeight
print(ans)
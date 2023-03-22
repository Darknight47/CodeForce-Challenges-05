"""
------- Link for the challenge: https://codeforces.com/problemset/problem/1740/B -------------

Pak Chanek has n two-dimensional slices of cheese. The i-th slice of cheese can 
be represented as a rectangle of dimensions a(i) × b(i). 
We want to arrange them on the two-dimensional plane such that:

* Each edge of each cheese is parallel to either the x-axis or the y-axis.
* The bottom edge of each cheese is a segment of the x-axis.
* No two slices of cheese overlap, but their sides can touch.
* They form one connected shape.

Note that we can arrange them in any order (the leftmost slice of cheese is not necessarily 
the first slice of cheese). Also note that we can rotate each slice of cheese in any way 
as long as all conditions still hold.

Find the minimum possible perimeter of the constructed shape.

Input
Each test contains multiple test cases. The first line contains an integer t
(1 ≤ t ≤ 2⋅10^4) — the number of test cases. The following lines contain the 
description of each test case.

The first line of each test case contains an integer n
(1 ≤ n ≤ 2⋅10^5) — the number of slices of cheese Pak Chanek has.

The i-th of the next n lines of each test case contains two integers a(i) 
and b(i)(1 ≤ a(i) , b(i) ≤ 10^9) — the dimensions of the i-th slice of cheese.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a line containing an integer representing 
the minimum possible perimeter of the constructed shape.

Input:
3
4
4 1
4 5
1 1
2 3
3
2 4
2 6
2 3
1
2 65

Output:
26
24
134

"""
cases = int(input())
for i in range(cases):
    bits = int(input())
    maxHeight = 0
    arr = []
    for j in range(bits):
        a, b = map(int, input().split())
        tempTuple = (a, b)
        arr.append(tempTuple)
        w = 0
        if(a > maxHeight):
            maxHeight = a
        if(b > maxHeight):
            maxHeight = b
    for elem in arr:
        w += min(elem)
    ans = 2 * (w + maxHeight)
    print(ans)    
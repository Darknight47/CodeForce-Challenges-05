"""
----------- https://codeforces.com/problemset/problem/1686/A -------------
You are given an array of n integers a1,a2,…,an.
After you watched the amazing film "Everything Everywhere All At Once", you came up with the following operation.

In one operation, you choose n−1 elements of the array and replace each of them with their arithmetic mean
(which doesn't have to be an integer). For example, from the array [1,2,3,1] we can get the array [2,2,2,1],
if we choose the first three elements, or we can get the array [43,43,3,43], 
if we choose all elements except the third.

Is it possible to make all elements of the array equal by performing a finite number of such operations?

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 200)  — 
the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 50)  — the number of integers.

The second line of each test case contains n integers a1,a2,…,an (0 ≤ a(i) ≤ 100).

Output
For each test case, if it is possible to make all elements equal after some number of operations, output YES.
Otherwise, output NO.

You can output YES and NO in any case (for example, strings yEs, yes, Yes will be recognized as a positive response).

"""

cases = int(input())
for i in range(cases):
    ok = False
    sze = int(input())
    lst = list(map(int, input().split()))
    totalSum = sum(lst)
    for t in range(sze):
        tempNum = lst[t]
        tempSum = totalSum - tempNum
        tempMean = tempSum / (sze - 1)
        if(tempMean == tempNum):
            ok = True
            break
    print("YES" if ok else "NO")
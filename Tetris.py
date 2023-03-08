"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1324/A ----------

You are given some Tetris field consisting of n columns. 
The initial height of the i-th column of the field is a(i) blocks. 
On top of these columns you can place only figures of size 2×1
(i.e. the height of this figure is 2 blocks and the width of this figure is 1 block). 
Note that you cannot rotate these figures.

Your task is to say if you can clear the whole field by placing such figures.

More formally, the problem can be described like this:

The following process occurs while at least one a(i) is greater than 0:

You place one figure 2×1 (choose some i from 1 to n and replace a(i) with a(i)+2 );
then, while all a(i) are greater than zero, replace each a(i) with a(i)−1.

And your task is to determine if it is possible to clear the whole field 
(i.e. finish the described process), choosing the places for new figures properly.

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1 ≤ t ≤ 100) — the number of test cases.

The next 2(t) lines describe test cases. The first line of the test case contains one integer n (1 ≤ n ≤ 100) — 
the number of columns in the Tetris field. The second line of the test case contains n
integers a1,a2,…,an (1 ≤ a(i) ≤ 100 ), where a(i) is the initial height of the i-th column of the Tetris field.

Output
For each test case, print the answer — "YES" (without quotes) 
if you can clear the whole Tetris field and "NO" otherwise.

Input:
4
3
1 1 3
4
1 1 2 1
2
11 11
1
100

Output:
YES
NO
YES
YES
"""
sze = int(input())
for i in range(sze):
    columns = int(input())
    lst = list(map(int, input().split()))
    even = False
    odd = False
    ans = ""
    for num in lst:
        if(num % 2 == 0):
            even = True
        else:
            odd = True
    if(even and odd):
        ans = "NO"
    else:
        ans = "YES"
    print(ans)
"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/734/B -----

Recently Anton found a box with digits in his room. There are k2 digits 2, 
k3 digits 3, k5 digits 5 and k6 digits 6.

Anton's favorite integers are 32 and 256. He decided to compose this integers 
from digits he has. He wants to make the sum of these integers as large as possible. 
Help him solve this task!

Each digit can be used no more than once, i.e. the composed integers should 
contain no more than k2 digits 2, k3 digits 3 and so on. Of course, unused 
digits are not counted in the sum.

Input
The only line of the input contains four integers k2, k3, k5 and k6 — the 
number of digits 2, 3, 5 and 6 respectively (0 ≤ k2, k3, k5, k6 ≤ 5·10^6).

Output
Print one integer — maximum possible sum of Anton's favorite integers that 
can be composed using digits from the box.

"""
k2, k3, k5, k6 = map(int, input().split())
temp1 = min(k2, k5, k6)
temp2 = min((k2 - temp1), k3)
ans = temp1 * 256 + temp2 * 32
print(ans)
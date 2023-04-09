"""
------- Link for the challenge: https://codeforces.com/contest/818/problem/A ---------

There are n students who have taken part in an olympiad. Now it's time to award the students.

Some of them will receive diplomas, some wiil get certificates, and others won't receive anything. 
Students with diplomas and certificates are called winners. But there are some rules of counting the 
number of diplomas and certificates. The number of certificates must be exactly k times greater than 
the number of diplomas. The number of winners must not be greater than half of the number of all students 
(i.e. not be greater than half of n). It's possible that there are no winners.

You have to identify the maximum possible number of winners, according to these rules. 
Also for this case you have to calculate the number of students with diplomas, the number of students with 
certificates and the number of students who are not winners.

Input
The first (and the only) line of input contains two integers n and k (1 ≤ n, k ≤ 10^12), where n is the number 
of students and k is the ratio between the number of certificates and the number of diplomas.

Output
Output three numbers: the number of students with diplomas, the number of students with certificates 
and the number of students who are not winners in case when the number of winners is maximum possible.

Input:
18 2

Output:
3 6 9
"""
n, k = map(int, input().split())
t1 = n // 2
t2 = k + 1
a = t1 // t2
b = a * k
c = n - (a + b)
print(a,b,c)
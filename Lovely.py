"""
----- Link for the challenge: https://codeforces.com/contest/688/problem/B --------

Pari has a friend who loves palindrome numbers. A palindrome number is a number 
that reads the same forward or backward. For example 12321, 100001 and 1 are 
palindrome numbers, while 112 and 1021 are not.

Pari is trying to love them too, but only very special and gifted people can 
understand the beauty behind palindrome numbers. Pari loves integers with even 
length (i.e. the numbers with even number of digits), so she tries to see a lot 
of big palindrome numbers with even length (like a 2-digit 11 or 6-digit 122221), 
so maybe she could see something in them.

Now Pari asks you to write a program that gets a huge integer n from the input 
and tells what is the n-th even-length positive palindrome number?

Input
The only line of the input contains a single integer n (1 ≤ n ≤ 10100 000).

Output
Print the n-th even-length palindrome number.

Input: 
1

Output:
11
"""
n = input()
ans = ""
if(len(n) == 1):
    ans = n + n
else:
    rev = n[::-1]
    ans = n + rev
print(ans)
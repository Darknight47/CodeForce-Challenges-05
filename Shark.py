"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/621/A ------------

Today, Wet Shark is given n integers. Using any of these integers no more than once,
Wet Shark wants to get maximum possible even (divisible by 2) sum. Please, calculate this value for Wet Shark.

Note, that if Wet Shark uses no integers from the n integers, the sum is an even integer 0.

Input
The first line of the input contains one integer, n (1 ≤ n ≤ 100 000).
The next line contains n space separated integers given to Wet Shark.
Each of these integers is in range from 1 to 109, inclusive.

Output
Print the maximum possible even sum that can be obtained if we use some of the given integers.

Input:
3
1 2 3

Output:
6

"""
sze = int(input())
lst = sorted(list(map(int, input().split())))
totalSum = sum(lst)
if(totalSum % 2 == 0):
    print(totalSum)
else:
    for num in lst:
        totalTemp = totalSum - num
        if(totalTemp % 2 == 0):
            print(totalTemp)
            break

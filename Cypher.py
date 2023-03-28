"""
-------------- Link for the challenge: https://codeforces.com/contest/1703/problem/C ------------

Luca has a cypher made up of a sequence of n wheels, each with a digit a(i) written on it. 
On the i-th wheel, he made b(i) moves. Each move is one of two types:

up move (denoted by U): it increases the i-th digit by 1. 
After applying the up move on 9, it becomes 0.down move (denoted by D): 
it decreases the i-th digit by 1. After applying the down move on 0, it becomes 9.

Luca knows the final sequence of wheels and the moves for each wheel. Help him find the original 
sequence and crack the cypher.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the number of wheels.

The second line contains n integers a(i) (0 ≤ a(i) ≤ 9) — the digit shown on the i-th wheel after all 
moves have been performed.

Then n lines follow, the i-th of which contains the integer b(i) (1 ≤ b(i) ≤ 10) and b(i) characters 
that are either U or D — the number of moves performed on the i-th wheel, and the moves performed. 
U and D represent an up move and a down move respectively.

Output
For each test case, output n space-separated digits  — the initial sequence of the cypher.

Input:
3
3
9 3 1
3 DDD
4 UDUU
2 DU
2
0 9
9 DDDDDDDDD
9 UUUUUUUUU
5
0 5 9 8 3
10 UUUUUUUUUU
3 UUD
8 UUDUUDDD
10 UUDUUDUDDU
4 UUUU

Output:
2 1 1 
9 0 
0 4 9 6 9 

"""
cases = int(input())
for i in range(cases):
    wheels = int(input())
    lst = list(map(int, input().split()))
    ans = []
    for j in range(wheels):
        wheelNum = lst[j]
        tr, tempInfo = map(str, input().split())
        tempRotation = int(tr)
        for w in range(tempRotation):
            tempAction = tempInfo[w]
            if(tempAction == 'D'): #Go Up.
                wheelNum += 1
                if(wheelNum >= 10):
                    wheelNum = 0
            elif(tempAction == 'U'): #Go Down.
                wheelNum -= 1
                if(wheelNum < 0):
                    wheelNum = 9
        ans.append(wheelNum)
    print(*ans)
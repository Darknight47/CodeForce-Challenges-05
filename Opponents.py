"""
------ Link for the challenge: https://codeforces.com/contest/688/problem/A -------

Arya has n opponents in the school. Each day he will fight with all opponents who are present this day. 
His opponents have some fighting plan that guarantees they will win, but implementing this plan requires 
presence of them all. That means if one day at least one of Arya's opponents is absent at the school, 
then Arya will beat all present opponents. Otherwise, if all opponents are present, then they will beat Arya.

For each opponent Arya knows his schedule — whether or not he is going to present on each particular day. 
Tell him the maximum number of consecutive days that he will beat all present opponents.

Note, that if some day there are no opponents present, Arya still considers he beats all the present opponents.

Input
The first line of the input contains two integers n and d (1 ≤ n, d ≤ 100) — the number of opponents 
and the number of days, respectively.

The i-th of the following d lines contains a string of length n consisting of characters '0' and '1'. 
The j-th character of this string is '0' if the j-th opponent is going to be absent on the i-th day.

Output
Print the only integer — the maximum number of consecutive days that Arya will beat all present opponents.

Input:
2 2
10
00

Output:
2
"""
n, d = map(int, input().split())
ans = 0
consMax = 0
for i in range(d):
    strTemp = input()
    setTemp = set(strTemp)
    if(len(setTemp) == 1 and list(setTemp)[0] == '0'):
        consMax += 1
    elif(len(setTemp) > 1):
        consMax += 1
    else:        
        if(consMax > ans):
            ans = consMax
        consMax = 0
if(consMax > ans):
    ans = consMax
print(ans)
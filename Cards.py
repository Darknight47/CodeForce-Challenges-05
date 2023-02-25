"""
------ Link for the challenge: https://codeforces.com/problemset/problem/680/A ------------
A little bear Limak plays a game. He has five cards. There is one number written on each card.
Each number is a positive integer.

Limak can discard (throw out) some cards. His goal is to minimize the sum of numbers written on remaining
(not discarded) cards.

He is allowed to at most once discard two or three cards with the same number.
Of course, he won't discard cards if it's impossible to choose two or three cards with the same number.

Given five numbers written on cards, cay you find the minimum sum of numbers on remaining cards?

Input
The only line of the input contains five integers t1, t2, t3, t4 and t5 (1 ≤ t(i) ≤ 100) — numbers written on cards.

Output
Print the minimum possible sum of numbers written on remaining cards.

Input:
7 3 7 3 20

Output:
26

"""
lst = list(map(int, input().split()))
diction = {}
for tempKey in lst:
    diction.setdefault(tempKey, 0)
    tempValue = diction[tempKey] + 1
    diction[tempKey] = tempValue
ans = 0
dictionSze = len(diction)
if(dictionSze == 1):
    ans = lst[0] + lst[1]
else:
    temp3 = 0
    temp2 = 0
    temp2Max = 0
    tt = 0
    tempTotalMax = 0
    for temp in diction:
        tv = diction[temp]
        if(tv >= 3):
            for s in range(3):
                temp3 += temp
        elif(tv == 2):
            for j in range(tv):
                temp2 += temp
            temp2Max = max(temp2, tt)       
            tt = temp2
            temp2 = 0
    tempTotalMax = max(temp2Max, temp3)
    ans = abs(sum(lst) - tempTotalMax)
print(ans)
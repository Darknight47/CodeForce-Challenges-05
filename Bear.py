"""
------- Link for the challenge: https://codeforces.com/contest/658/problem/A --------

Limak and Radewoosh are going to compete against each other in the upcoming algorithmic contest. 
They are equally skilled but they won't solve problems in the same order.

There will be n problems. The i-th problem has initial score pi and it takes exactly ti minutes to solve it. 
Problems are sorted by difficulty — it's guaranteed that p(i) < p(i) + 1 and t(i) < t(i) + 1.

A constant c is given too, representing the speed of loosing points. Then, submitting the i-th problem at time 
x (x minutes after the start of the contest) gives max(0,  p(i) - c·x) points.

Limak is going to solve problems in order 1, 2, ..., n (sorted increasingly by p(i)). 
Radewoosh is going to solve them in order n, n - 1, ..., 1 (sorted decreasingly by p(i)). 
Your task is to predict the outcome — print the name of the winner (person who gets more points at the end) 
or a word "Tie" in case of a tie.

You may assume that the duration of the competition is greater or equal than the sum of all t(i). 
That means both Limak and Radewoosh will accept all n problems.

Input
The first line contains two integers n and c (1 ≤ n ≤ 50, 1 ≤ c ≤ 1000) — 
the number of problems and the constant representing the speed of loosing points.

The second line contains n integers p1, p2, ..., pn (1 ≤ p(i) ≤ 1000, p(i) < p(i) + 1) — initial scores.

The third line contains n integers t1, t2, ..., tn (1 ≤ t(i) ≤ 1000, t(i) < t(i) + 1) 
where t(i) denotes the number of minutes one needs to solve the i-th problem.

Output
Print "Limak" (without quotes) if Limak will get more points in total. Print "Radewoosh" (without quotes) 
if Radewoosh will get more points in total. Print "Tie" (without quotes) if Limak and Radewoosh will get 
the same total number of points.

Input:
3 2
50 85 250
10 15 25
Output:
Limak

"""
n, c = map(int, input().split())
scores = list(map(int, input().split()))
minutes = list(map(int, input().split()))
limak = 0
limakTotalTime = 0
radewoosh = 0
radewooshTotalTime = 0
for i in range(n):
    tempScore = scores[i]
    tempMin = minutes[i]
    limakTotalTime += tempMin
    tempValue = tempScore - (c * limakTotalTime)
    tempSum = max(0, tempValue)
    limak += tempSum
for j in range(n - 1, -1, -1):
    ts = scores[j]
    tm = minutes[j]
    radewooshTotalTime += tm
    tv = ts - (c * radewooshTotalTime)
    ts = max(0, tv)
    radewoosh += ts
if(limak > radewoosh):
    print("Limak")
elif(limak < radewoosh):
    print("Radewoosh")
else:
    print("Tie")
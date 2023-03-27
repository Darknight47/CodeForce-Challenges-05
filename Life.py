"""
------------ Link for the challenge: https://codeforces.com/contest/472/problem/B -------------

One way to create a task is to learn from life. You can choose some experience in real life, 
formalize it and then you will get a new task.

Let's think about a scene in real life: there are lots of people waiting in front of the elevator, 
each person wants to go to a certain floor. We can formalize it in the following way. 
We have n people standing on the first floor, the i-th person wants to go to the f(i)-th floor. 
Unfortunately, there is only one elevator and its capacity equal to k 
(that is at most k people can use it simultaneously). Initially the elevator is located on the first floor. 
The elevator needs |a - b| seconds to move from the a-th floor to the b-th floor 
(we don't count the time the people need to get on and off the elevator).

What is the minimal number of seconds that is needed to transport all the people to the 
corresponding floors and then return the elevator to the first floor?

Input:
The first line contains two integers n and k (1 ≤ n, k ≤ 2000) — the number of people and the maximal 
capacity of the elevator.

The next line contains n integers: f1, f2, ..., fn (2 ≤ f(i) ≤ 2000), where f(i) denotes the target 
floor of the i-th person.

Output:
Output a single integer — the minimal time needed to achieve the goal.

Input:
3 2
2 3 4
Output:
8
"""
people, capacity = map(int, input().split())
lst = sorted(list(map(int, input().split())))
tempTime = 0
while(len(lst) > 0):
    tempArr = []
    for i in range(capacity):
        if(len(lst) > 0):
            tempArr.append(lst.pop())
    tempArr = sorted(tempArr)
    if(len(tempArr) < 0):
        break
    tempTime += abs(tempArr[0] - 1)
    for i in range(len(tempArr) - 1):
        first = tempArr[i]
        second = tempArr[i + 1]
        tempTime += abs(second - first)
    tempTime += abs(tempArr[len(tempArr) - 1] - 1)
print(tempTime)
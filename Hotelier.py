"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1200/A ------------

Amugae has a hotel consisting of 10 rooms. The rooms are numbered from 0 to 9 from left to right.

The hotel has two entrances — one from the left end, and another from the right end. 
When a customer arrives to the hotel through the left entrance, they are assigned to an 
empty room closest to the left entrance. Similarly, when a customer arrives at the hotel 
through the right entrance, they are assigned to an empty room closest to the right entrance.

One day, Amugae lost the room assignment list. Thankfully Amugae's memory is perfect, 
and he remembers all of the customers: when a customer arrived, from which entrance, 
and when they left the hotel. Initially the hotel was empty. Write a program that 
recovers the room assignment list from Amugae's memory.

Input
The first line consists of an integer n (1 ≤ n ≤ 10^5), the number of events in Amugae's memory.

The second line consists of a string of length n describing the events in chronological order. 
Each character represents:

'L': A customer arrives from the left entrance.
'R': A customer arrives from the right entrance.
'0', '1', ..., '9': The customer in room x (0, 1, ..., 9 respectively) leaves.

It is guaranteed that there is at least one empty room when a customer arrives, 
and there is a customer in the room x when x (0, 1, ..., 9) is given. Also, all the rooms are initially empty.

Output
In the only line, output the hotel room's assignment status, from room 0 to room 9. 
Represent an empty room as '0', and an occupied room as '1', without spaces.

Input:
8
LLRL1RL1

Output:
1010000011
"""
sze = int(input())
lst = list(input())
rooms = [0] * 10
for ch in lst:
    if(ch == "L"):
        for i in range(10):
            if(rooms[i] == 0):
                rooms[i] = 1
                break
    elif(ch == "R"):
        for j in range(9, -1, -1):
            if(rooms[j] == 0):
                rooms[j] = 1
                break
    elif(ch.isnumeric()):
        rumTemp = int(ch)
        rooms[rumTemp] = 0
print(''.join([str(i) for i in rooms]))  

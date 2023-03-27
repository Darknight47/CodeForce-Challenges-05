"""
--------- Link for the challenge: https://codeforces.com/contest/78/problem/B ---------

The Easter Rabbit laid n eggs in a circle and is about to paint them.

Each egg should be painted one color out of 7: red, orange, yellow, green, blue, indigo or violet. 
Also, the following conditions should be satisfied:

 *   Each of the seven colors should be used to paint at least one egg.
 *   Any four eggs lying sequentially should be painted different colors.
    
Help the Easter Rabbit paint the eggs in the required manner. We know that it is always possible.

Input
The only line contains an integer n — the amount of eggs (7 ≤ n ≤ 100).

Output
Print one line consisting of n characters. The i-th character should describe 
the color of the i-th egg in the order they lie in the circle. The colors should be represented as 
follows: "R" stands for red, "O" stands for orange, "Y" stands for yellow, "G" stands for green, 
"B" stands for blue, "I" stands for indigo, "V" stands for violet.

If there are several answers, print any of them.

Input:
8
Output:
ROYGRBIV

"""
n = int(input())
arr = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']
diff = n - 7
colours = [""] * n
for i in range(7):
    if(i == 0):
        colours[i] = 'R'
    elif(i == 1):
        colours[i] = 'O'
    elif(i == 2):
        colours[i] = 'Y'
    elif(i == 3):
        colours[i] = 'G'
    elif(i == 4):
        colours[i] = 'B'
    elif(i == 5):
        colours[i] = 'I'
    elif(i == 6):
        colours[i] = 'V'
for j in range(7, n, 1):
    currentIndx = j
    t1 = colours[currentIndx - 1]
    t2 = colours[currentIndx - 2]
    t3 = colours[currentIndx - 3]
    t4 = colours[0]
    t5 = colours[1]
    t6 = colours[2]
    targetColour = ""
    for z in arr:
        if(z != t1 and z != t2 and z != t3 and z != t4 and
           z != t5 and z!= t6):
            targetColour = z
            break
    colours[currentIndx] = targetColour
print("".join(colours))
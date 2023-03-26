"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/900/A ----------

You have n distinct points on a plane, none of them lie on OY axis. 
Check that there is a point after removal of which the remaining points are located on one side of the OY axis.

Input
The first line contains a single positive integer n (2 ≤ n ≤ 10^5).

The following n lines contain coordinates of the points. The i-th of these lines contains two 
single integers xi and yi (|xi|, |yi| ≤ 10^9, xi ≠ 0). No two points coincide.

Output
Print "Yes" if there is such a point, "No" — otherwise.

You can print every letter in any case (upper or lower).

Input:
3
1 1
-1 -1
2 -1

Output:
YES

"""
cases = int(input())
positives = []
negatives = []
for i in range(cases):
    x, y = map(int, input().split())
    if(x > 0):
        positives.append((x, y))
    else:
        negatives.append((x, y))
if(len(positives) == 1 or len(negatives) == 1):
    ans = "YES"
elif(len(positives) > 0 and len(negatives) == 0):
    ans = "YES"
elif(len(negatives) > 0 and len(positives) == 0):
    ans = "YES"
else:
    ans = "NO"
print(ans)
"""
---------- Link for the challenge: https://codeforces.com/contest/658/problem/B ------------

Limak is a little polar bear. He loves connecting with other bears via social networks. 
He has n friends and his relation with the i-th of them is described by a unique integer t(i). 
The bigger this value is, the better the friendship is. No two friends have the same value t(i).

Spring is starting and the Winter sleep is over for bears. Limak has just woken up and logged in. 
All his friends still sleep and thus none of them is online. Some (maybe all) of them will appear 
online in the next hours, one at a time.

The system displays friends who are online. On the screen there is space to display at most k friends. 
If there are more than k friends online then the system displays only k best of them — those with biggest t(i).

Your task is to handle queries of two types:

"1 id" — Friend id becomes online. It's guaranteed that he wasn't online before.
"2 id" — Check whether friend id is displayed by the system. Print "YES" or "NO" in a separate line.
Are you able to help Limak and answer all queries of the second type?

Input
The first line contains three integers n, k and q (1 ≤ n, q ≤ 150 000, 1 ≤ k ≤ min(6, n)) — the number of friends, 
the maximum number of displayed online friends and the number of queries, respectively.

The second line contains n integers t1, t2, ..., tn (1 ≤ t(i) ≤ 109) where ti describes how good is Limak's 
relation with the i-th friend.

The i-th of the following q lines contains two integers typei and idi (1 ≤ type i ≤ 2, 1 ≤ i d(i) ≤ n) — 
the i-th query. If typei = 1 then a friend idi becomes online. If typei = 2 then you should check whether 
a friend idi is displayed.

It's guaranteed that no two queries of the first type will have the same idi becuase one friend can't '
become online twice. Also, it's guaranteed that at least one query will be of the second type (type i = 2) 
so the output won't be empty.

Output
For each query of the second type print one line with the answer — "YES" (without quotes) 
if the given friend is displayed and "NO" (without quotes) otherwise.

Input:
4 2 8
300 950 500 200
1 3
2 4
2 3
1 1
1 2
2 1
2 2
2 3

Output:
NO
YES
NO
YES
YES

"""
friends, displays, queries = map(int, input().split())
lst = list(map(int, input().split()))
screen = []
awakes = []
for j in range(queries):
    t, indx = map(int, input().split())
    if(t == 1):
        indxTemp = indx - 1
        temp = lst[indxTemp]
        if(len(awakes) < displays):
            awakes.append(temp)
        else:
            awakes = sorted(awakes)
            for w in range(displays):
                if(temp > awakes[w]):
                    awakes[w] = temp
                    break    
    else:
        tt = lst[indx - 1]
        if(awakes.count(tt) > 0):
            print("YES")
        else:
            print("NO")
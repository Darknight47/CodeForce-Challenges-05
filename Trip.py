"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1113/A ---------

Sasha is a very happy guy, that's why he is always on the move.
There are n cities in the country where Sasha lives. They are all located on one straight line,
and for convenience, they are numbered from 1 to n in increasing order. The distance between any two adjacent cities is equal to 1 kilometer.
Since all roads in the country are directed,
it's possible to reach the city y from the city x only if x < y.

Once Sasha decided to go on a trip around the country and to visit all n
cities. He will move with the help of his car, Cheetah-2677.
The tank capacity of this model is v liters, and it spends exactly 1
liter of fuel for 1 kilometer of the way. At the beginning of the journey, the tank is empty.
Sasha is located in the city with the number 1 and wants to get to the city with the number n.
There is a gas station in each city.
In the i -th city, the price of 1 liter of fuel is i dollars.
It is obvious that at any moment of time, the tank can contain at most v liters of fuel.

Sasha doesn't like to waste money,
that's why he wants to know what is the minimum amount of money is needed to
finish the trip if he can buy fuel in any city he wants. Help him to figure it out!

Input
The first line contains two integers n and v (2 ≤ n ≤ 100, 1 ≤ v ≤ 100)  —
the number of cities in the country and the capacity of the tank.

Output
Print one integer — the minimum amount of money that is needed to finish the trip.
"""
n, v = map(int, input().split())
tank = v
visited = 1
cost = visited * v
if(v >= n):
    cost = n - 1
else:
    while (visited < n):
        visited += 1
        tank -= 1
        diff = n - visited
        if(diff > tank):
            diffTank = v - tank
            tank += diffTank
            cost += (visited * diffTank)
print(cost)
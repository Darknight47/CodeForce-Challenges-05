"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/137/A ----------

Polycarpus has postcards and photos hung in a row on the wall. 
He decided to put them away to the closet and hang on the wall a 
famous painter's picture. Polycarpus does it like that: he goes from 
the left to the right and removes the objects consecutively. 
As Polycarpus doesn't want any mix-ups to happen, he will not carry in his hands 
objects of two different types. In other words, Polycarpus can't carry both postcards 
and photos simultaneously. Sometimes he goes to the closet and puts the objects there, 
thus leaving his hands free. Polycarpus must put all the postcards and photos to the closet. 
He cannot skip objects. What minimum number of times he should visit the closet if he cannot 
carry more than 5 items?

Input
The only line of the input data contains a non-empty string consisting of letters "С" 
and "P" whose length does not exceed 100 characters. If the i-th character in the 
string is the letter "С", that means that the i-th object (the numbering goes from the left to the right) 
on Polycarpus' wall is a postcard. And if the i-th character is the letter "P", 
than the i-th object on the wall is a photo.

Output:
Print the only number — the minimum number of times Polycarpus has to visit the closet.

Input:
CPCPCPC
Output:
7
"""
s = list(input().strip())
i = 0
ans = 0
while i < len(s):
    count = 1 # start with a count of 1 for the current character
    if((i+1) < len(s)):
        for j in range(i+1, i+5):
            if(j < len(s)):
                if s[i] == s[j]:
                    count += 1 # increment the count for each matching character
                else:
                    break # stop counting when a different character is found
    i += count # move to the next character after the sequence
    ans += 1
print(ans)
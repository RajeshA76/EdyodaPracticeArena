"""
You will be given a list you have to find sum of 2nd greatest and 2nd smallest elemnts.

Input Format:

First line will have space separated elements of list.

Output Format:

it will be an integer (sum)

Sample Input 0:

1 2 3 4 5 6

Sample Output 0:

7
"""
l = list(map(int, input().split()))
# Write your code here
l_max = max(l)
l_min = min(l)
l.remove(l_max)
l.remove(l_min)
sum = max(l) + min(l)


print(sum)
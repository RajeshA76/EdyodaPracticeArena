"""
 Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
 Including limit.
 For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20

which is equal to 98.

Input Format:

given_limit containing limit

Output Format:

print the sum as stated in description

Sample Input 0:

20
Sample Output 0:

98
"""

given_limit = int(input())
l = []
def multiple_task(limit):
# Write your code here
	for i in range(given_limit + 1):
		if i % 3 == 0 and i % 5 == 0:
			l.append(i)
		elif i % 3 == 0:
			l.append(i)
		elif i % 5 == 0:
			l.append(i)
			
multiple_task(given_limit)
print(sum(l))
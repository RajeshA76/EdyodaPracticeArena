"""
You will be given a string. You have to count the number of characters (character frequency) in a string.

Input Format:

One line containing a string

Output Format:

You have to print result as a string enclosed by "{" and "}"

Sample Input 0:

Edyoda123
Sample Output 0:

{'E': 1, 'd': 2, 'y': 1, 'o': 1, 'a': 1, '1': 1, '2': 1, '3': 1}
"""

s = input()
# Write your code here
dict = {}
for i in s:
	count = 0
	for j in s:
		if i == j:
			count += 1
	dict[i] = count
print(dict)

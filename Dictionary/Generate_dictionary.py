"""
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

Input Format:

You will be given an integer (n).

Output Format:

You have to print dictionary

Sample Input 0:

2
Sample Output 0:

{1: 1, 2: 4}
"""

n = int(input())
# Write your code here
dict = {}
if n == 0:
	dict = {0:0}
else:
	for i in range(1,n + 1):
		dict[i] = i*i
	
print(dict)
#!/usr/bin/env python3
"""
You will have number or elements and next n lines containing list elements. You have to create list from that given string.

Input Format:

In first-line it will have an integer (numbers of elements inside a list). In the second line, it will have a string containing space separated list elements.

Output Format:

A single line containing a list.

Sample Input 0:

5
abda
defd
123
Edyoda
Saas
Sample Output 0:

['abda','defd',123,'Edyoda','Saas']
"""
n = int(input())
# Write your code here
list = []
for i in range(n):
	inp = input()
	list.append(inp)
	
print(list)
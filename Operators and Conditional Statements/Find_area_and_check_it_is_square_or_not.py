#Question
"""
Take values of length and breadth of a rectangle from the user and check it is square or not. Return area of a rectangle.
 
Input Format:
There will be two lines each will contain a single integer. The first line contains length and the second line contains width. 
 
Output Format:
There will be two lines the first will contain boolean True or False and the second will contain an integer that would be the area of a rectangle.
 
Sample Input 0:
5
5
 
Sample Output 0:
True
25

"""
#Solution: 
length = int(input())
breadth = int(input())

# Write your code here

import math

area = length * breadth

decimal = math.sqrt(area)
integer = int(decimal)
if integer == decimal:
	print(True)
	print(area)
else:
	print(False)
	print(area)
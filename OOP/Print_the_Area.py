"""
Use the class given to calculate the area based on upon the shape. Start with making an object of Class Area and than Playing with it for different shapes.

Input Format:

shape and l,b or r depending upon the shape

Output Format:

area of the shape

Sample Input 0:

circle
4
Sample Output 0:

50
"""

import math
class Area:
    def rectangle(self,l,b):
        print(l*b)
    def circle(self,r):
        circle_area = math.pi*(r**2)
        circle_area_rounded = round(circle_area)
        print(circle_area_rounded)

shape = input()

if shape == "circle":
    r = int(input())
else:
    l,b = map(int,input().split())
# Write your code here
A = Area()
if shape == "circle":
	A.circle(r)
else:
	A.rectangle(l,b)
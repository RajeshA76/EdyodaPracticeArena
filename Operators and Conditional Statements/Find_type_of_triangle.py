#Question
"""
Given the 3 sides of a triangle – x, y and z – determine whether the triangle is equilateral, isosceles or obtuse.

Input Format:

Three lines, each line contains an integer one side of triangle

Output Format:

Print type of triangle equilateral, isosceles, or obtuse

Sample Input 0:

5
6
7
Sample Output :

obtuse
"""
#Solution

x = int(input())
y = int(input())
z = int(input())
# Write your code here
if x == y and y == z and x ==z:
	print("equilateral")
elif x != y and y != z and x != z:
	print("obtuse")
else:
	print("isosceles")

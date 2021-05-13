#Question
"""
Write a Python program that accepts the radius of a circle from the user and compute the area.
 
Input Format:
There will be one line containing a single integer.
 
Output Format:
There will be one line containing a float number.
 
Sample Input 0:
5
 
Sample Output 0:
78.5
"""
#Solution:

radius = int(input())

# Write your code here
pi = 3.14
area = pi * pow(radius,2)
print(area)
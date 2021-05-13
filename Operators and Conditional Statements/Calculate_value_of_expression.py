#Question
"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
 
For Example: n = 5 Then expression would be 5+55+555 and answer would be 615
 
Input Format:
There will be one line containing a single integer.
 
Output Format:
There will be one line containing a integer number.
 
Sample Input 0:
5
 
Sample Output 0:
615
"""
#Solution:

n = int(input())
# Write your code here
string = str(n)
list =[]
for i in range(3):
	if i == 0:
		list.append(string)
	elif i > 0:
		list.append(string * (i + 1))

sum = 0

for i in list:
	sum = sum + int(i)

print(sum)

"""
You will be given a digti. You have to find sum of digits. But there is one secial condition that you have to keep calculating sum unle you get one digit answer.

For Example: 

digit = 25643

sum of digits of 2+5+6+4+3 = 20

Here 20 is 2 digit number so you have to find sum of digits of 20 again and final answer would be 2+0 = 2

Input Format:

The first line contains an integer.

Output Format:

Print anser in integer format

Sample Input 0:

25643

Sample Output 0:

2
"""

n = int(input())
# Write your code here use STDIN for inout and STDOUT for output
l = [int(i) for i in str(n)]
add = sum(l)
while add > 10:
	list = [int(i) for i in str(add)]
	add = sum(list)
	
print(add)
	
"""
Consider an integer x, create multiplication table of x,x+2,and x+3.Each multiplication table should have space separated values. All three table should be line separated.

Input Format:

A single integer x will be provided.

Output Format:

Output the multiplication table of x,x+2, and x+3 on 3 different lines. The internal Values of a table should be separated by space. No extra spaces at the end of the table.

Sample Input 0:

24

Sample Output 0:

24 48 72 96 120 144 168 192 216 240
26 52 78 104 130 156 182 208 234 260
27 54 81 108 135 162 189 216 243 270
"""


x = int(input())
# Write your code here
for j in [0,2,3]:
	for i in range(1,11):
		if i < 10:
			mulx = (x + j) * i
			print(mulx,end = " ")
		elif i == 10:
			mulx = (x + j) * i
			print(mulx)
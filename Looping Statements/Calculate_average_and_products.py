"""
Take inputs from the user until the user presses 'q'. Print average and product of all numbers.

Input Format:

There will be only one line contains string either a number or character 'q'.

Output Format:

There will be two lines the first line contains an integer( average of numbers) and the second contains an integer (product of numbers).

Sample Input 0:

5
10
15
20
q
Sample Output 0:

50
15000
"""

# Write your code here
list = []
while True:
	n = input()
	if n == 'q':
		break
	list.append(int(n))
mul = 1
if len(list) == 0:
	avg = 0
	mul = 0
else:
	avg = sum(list) // len(list)
	for i in list:
		mul = mul * i


print(avg)
"""
You will be given a string you have to change the case. if the character is in lowercase then make it in uppercase and vice-versa if if character is digit or special character then print itself.

Input Format:

One line containing string

Output Format:

Print your answer it should be a string

Sample Input 0:

Edyoda123
Sample Output 0:

eDYODA123
"""

s = input()
# Write your code here
res = ''
for i in s:
	if i.islower():
		res = res + i.upper()
	elif i.isupper():
		res = res + i.lower()
	else:
		res = res + i
print(res)
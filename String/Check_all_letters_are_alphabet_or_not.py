"""
You will be given a string.you have to check that all letters in the given string are alphabet it not?

Input Format:

only one line contains string

Output Format:

Print "True" or "False" without quotes.

Sample Input 0:

Edyoda123
Sample Output 0:

False
"""

s = input()
# Write your code here
res = "True"
for i in s:
	if not i.isalpha():
		res = "False"
		break;
print(res)
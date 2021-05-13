"""
You will be given a string you have to sort string lexicographically.

Lexicographically means a generalization of the way words are alphabetically ordered based on the alphabetical order of their component letters.

Input Format:
One line contains string

Output Format:
Print sorted string

Sample Input 0:
Edyoda123
 
Sample Output 0:
'123Eaddoy'
"""

s = input()
# Write your code here
num = ''
l_c = ''
u_c = ''
s_c = ''
for i in s:
	if i in '0123456789':
		num = num + i
	elif i.isupper():
		u_c = u_c + i
	elif i.islower():
		l_c = l_c + i
	else:
		s_c = s_c + i
lex =  sorted(num)+sorted(u_c)+sorted(l_c)
print(s_c+"".join(lex))		
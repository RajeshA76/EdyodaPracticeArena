"""
 Write a Python program to check the validity of password x input by users.

Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].

At least 1 number between [0-9].

At least 1 character from [$#@].

Minimum length 6 characters.

Maximum length 16 characters.

Input Format:

x as input password by user.

Output Format:

valid or not valid as according to above condition.

Input Sample:

python@3
Output Sample:

not valid
"""

x=input()
# Write your code here
upper = "False"
lower = "False"
num = "False"
sp_c = "False"
for i in x:
	if i.isupper():
		upper = "True"
	elif i.islower():
		lower = "True"
	elif i in "0123456789":
		num = "True"
	elif i in "$#@":
		sp_c = "True"
		
if len(x) >= 6 and len(x) <= 16:
	if upper == "True" and lower == "True" and num == "True" and sp_c == "True":
		print("valid")
	else:
		print("not valid")
else:
	print("not valid")

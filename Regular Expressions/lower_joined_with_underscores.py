"""
Write a Python program to find sequences of lowercase letters joined with a underscore.
Input Format:

input_string from the Standard input method.

Output Format:

True and False as described in the description

Sample Input 0:

alpha_nonumber
Sample Output 0:

True
"""

import re
input_string = input()
# Write your code here
s = re.search(r'[a-z]{1,}_[a-z]{1,}$',input_string)
if s:
	print(True)
else:
	print(False)
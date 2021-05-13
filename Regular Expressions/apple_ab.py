"""
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'. If matched return True else False.

Input Format:

input_string from the Standard input will be given

Output Format:

True or False based on the above description.

Sample Input 0:

apple_ab
Sample Output 0:

True
"""

import re
input_string = input()
# Write your code here
pattern = "a.*b$"
match = re.search(pattern,input_string)
if match:
	print(True)
else:
	print(False)
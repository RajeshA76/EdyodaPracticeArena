"""
Write a Python program that prints True if the input_string contains an "a" followed by 3 or more "b's" and prints False if it does not.

Input Format:

input_string will be given via standard input method.

Output Format:

Print True or False as in the description

Sample Input 0:

labbbra
Sample Output 0:

True
"""

input_string = input()
import re
# Write your code here
s = re.search(r'[a][b]{3,}',input_string)
if s:
	print(True)
else:
	print(False)
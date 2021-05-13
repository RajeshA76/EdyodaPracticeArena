"""
You will be given a string.you have to replace all the occurrence either in lower or upper case of the first character with '@'

Input Format:

only one line contains a string

Output Format:

Print new string.

Sample Input 0:

This is not difficult
Sample Output 0:

This is no@ difficul@
"""

s = input()
# Write your code here
result = ""
for i in s[1:]:
	if i.lower() == s[0].lower():
		result = s.replace(i,"@")
	
		
if result:
	print(result)
else:
	print(s)
"""
You will be given a string.you have to replace characters at odd index values with "A"

Input Format:

only one line contains string

Output Format:

Print result

Sample Input 0:

Edyoda123
Sample Output 0:

EAyAdA1A3
"""

s = input()
# Write your code here
list_s = [i for i in s]
for i in range(len(list_s)):
	if i % 2 != 0:
		list_s[i] = "A"
		
print(''.join(list_s))
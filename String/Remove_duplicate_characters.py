"""
You will be given a string.you have to remove all duplicate characters(Either in lower case or Upper case) from the given string.

Input Format:

only one line contains a string

Output Format:

Print new string without duplicate characters

Sample Input 0:

EDYoda123

Sample Output 0:

EDyoa123
"""

s = input()
# Write your code here
list = []
for i in range(len(s)-1):
	for j in range(i+1,len(s)):
		if s[i].lower() == s[j].lower():
			list.append(j)
		elif s[i] == s[j]:
			list.append(j)
new_list = []
for i in range(len(s)):
	if i not in list:
		new_list.append(i)
result = [s[i] for i in new_list]
print("".join(result))
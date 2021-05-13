"""
You will be given a string.you have to reverse the string if the length of a string is multiple of 4.

Input Format:

only one line contains a string

Output Format:

Print result

Sample Input 0:

Edyoda12
Sample Output 0:

21adoydE
"""

s = input()
# Write your code here
length = len(s)
len_initial = 0
if length % 4 == 0:
	for i in range(length - 1,len_initial - 1,-1):
		print(s[i],end="")
else:
	for i in range(len_initial,length):
		print(s[i],end="")
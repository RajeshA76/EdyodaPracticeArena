"""
You will be given to list main_list and sub_list. You have to check sublist presents in main list or not? 

Input Format:

Two lines containing string. First line will have space separated elements of main list and second line contains space separated elements of sub list.

Output Format:

Print True or False 

Sample Input 0:

a b c d
b c
Sample Output 0:

True
"""
main_list, sub_list = input().split() , input().split()
# Write your code here
new_sub = []
for i in sub_list:
	if i in main_list:
		new_sub.append(i)
		
if new_sub == sub_list:
	print(True)
else:
	print(False)
	
"""
You will be given two lists. You have to map these two lists into a dictionary

Input Format:

In first two lines conatining space seprated list elements.

Output Format:

Print THe dictionary

Sample Input 0:

name roll_number
david 123
Sample Output 0:

{'name':'david', 'roll_number':'123'}

"""


key_list = input().split()
value_list = input().split()
# Write your code here
dict = {}
length = len(key_list)
for i in range(length):
	dict[key_list[i]] = value_list[i]
	
print(dict)
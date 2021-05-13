"""
You will be given 2 different list of same length. you have to print common elements.

Input Format:

Two lines containing string. First line will have space separated elements of main list and second line contains space separated elements of sub list.

Output Format:

Print space seprated common elements

Sample Input 0:

a b c d
c d e f
Sample Output 0:

c d
"""

list_1, list_2 = input().split() , input().split()
# Write your code here
common = []
for i in list_1:
	if i in list_2 and i not in common:
		common.append(i)
		
ce = (" ").join(common)
print(ce)
		
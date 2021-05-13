"""
You will be given an integer(n) number key-value pair and in next n lines, you will be given space-separated key value. you have to create a dictionary from that given strings. After those n lines, there will be one more line containing the space-separated key value. You have to add that extra key value in that existing dictionary

Input Format:

The Frist line contains integer n and for next line contains space-separated key-values pair. in last it will contain that key value to be added in the existing dictionary.

Output Format:

Print the dictionary

Sample Input 0:

5
A 1
B 2
C 3
D 1
E 1
F 5
Sample Output 0:

{'A': '1', 'B': '2', 'C': '3', 'D': '1', 'E': '1', 'F': '5'}
"""

n = int(input())
# Write your code here
keys = []
values = []
for i in range(n + 1):
	inp = input().split()
	keys.append(inp[0])
	values.append(inp[1])

new_dict = {}
for i in range(len(keys)):
	new_dict[keys[i]] = values[i]
	
print(new_dict)

"""
You will be given an integer(n) number key-value pair and in next n lines, you will be given space-separated key value. you have to create a dictionary from that given strings. You have to track the count of the letters from the string.

Input Format:

The Frist line contains a string.

Output Format:

print the dictionary.

Sample Input 0:

Edyoda.com
Sample Output 0:

{'E': 1, 'd': 2, 'y': 1, 'o': 2, 'a': 1, '.': 1, 'c': 1, 'm': 1}
"""


# write your code here
inp = input()
dict = {}
for i in inp:
	count = 0
	for j in inp:
		if i == j:
			count += 1
		dict[i] = count
		
print(dict)
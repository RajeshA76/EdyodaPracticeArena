"""
You will be given an integer(n) number key-value pair and in next n lines, you will be given space-separated key value. you have to create a dictionary from that given strings. You have to print a sorted dictionary by values.

Input Format:

The Frist line contains integer n and for next line contains space-separated key-values pair. 

Output Format:

print sorted dictionary.

Sample Input 0:

4
a 2
b 0
c 5
d 6
Sample Output 0:

{'b': '0', 'a': '2', 'c': '5', 'd': '6'}
"""

# write your code here
n = int(input())
dict = {}
for i in range(n):
	inp = input().split()
	dict[inp[0]] = inp[1]
def sort(elem):
	return(dict[elem])
new_dict = {}
for i in sorted(dict,key=sort):
	new_dict[i] = dict[i]
print(new_dict)

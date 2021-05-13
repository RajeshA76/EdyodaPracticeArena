"""
You will have number of elements and in next n lines element of list. You have to create list from that given strings.. You have to sort the list based on 2nd last character of a string.
 
For example: given list = ['great','hello','hiyo','abc'] so your output_dictionary should be ['great', 'abc', 'hello','hiyo']
 
Input Format:
In first-line it will have an integer (numbers of elements inside a list). In the second line, it will have a string.
 
Output Format:
A single line containing a sorted list.
 
Sample Input 0:
4
great
abc
hello
hiyo
 
Sample Output 0:
['great', 'abc', 'hello','hiyo']
"""
n = int(input())
# Write your code here
list = []
def take_secondelem(elem):
	return elem[-2]
for i in range(n):
	inp = input()
	list.append(inp)
print(sorted(list,key=take_secondelem))
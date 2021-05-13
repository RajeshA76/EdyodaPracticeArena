"""
You will have number or elements and a string containing space separated tuples elements. You have to create list of tuples from that given string. You have to sort the list based on 2nd element of tuple.
 
For example: given list = [('zas',33),('abc',99),('dfg',2)] so your output_dictionary should be [('dfg',2),('zas',33),('abc',99)]
 
Input Format:
In first-line it will have an integer (numbers of elements inside a list). In the new n lines, it will have a tuple's element separated by space.
 
Output Format:
A single line containing sorted list.
 
Sample Input 0:
3
zas 33
abc 99
dfg 2
 
Sample Output 0:
[('dfg',2),('zas',33),('abc',99)]
"""
n = int(input())
# Write your code here
l = []
def second_element(elem):
	return(elem[1])
for i in range(n):
	inp = input().split()
	inp[1] = int(inp[1])
	l.append(tuple(inp))
	
print(sorted(l,key=second_element))
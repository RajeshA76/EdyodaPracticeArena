"""
You will be given an integer(n) number key-value pair and in next n lines, you will be given space-separated key value. you have to create a dictionary from that given strings. Find keys for the highest 3 values in a dictionary and print them in decreasing order of values.

Input Format:

The Frist line contains integer n and for next line contains space-separated key-values pair. 

Output Format:

print space-separated keys.

Sample Input 0:

4
a 2
b 0
c 5
d 6
Sample Output 0:

d c a
"""

# write your code here
n = int(input())
dict = {}
for i in range(n):
	inp = input().split()
	dict[inp[0]] = inp[1]
def sort(elem):
	return(dict[elem])

p = sorted(dict,key=sort,reverse=True)
print("{} {} {}".format(p[0],p[1],p[2]))

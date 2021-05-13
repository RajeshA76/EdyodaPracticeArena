"""
name and college is given, and function is restricted to take single argument *name. Inside the function write the code logic to print

name studies in college, here name and college are provided in input

Input Format:

name and college will be provided

Output Format:

name studies in college

Sample Input 0:

rohan mit
Sample Output 0:

rohan studies in mit
"""


name,college = map(str,input().split())

def test_fun(*name):
# Write your code here
	list = [i for i in name]
	print(list[0] + " studies in " + list[1])

test_fun(name,college)
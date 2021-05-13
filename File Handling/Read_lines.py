"""
You will be given a file name in the code editor itself and number of lines (n) you have to read the first n line from the given file and store them inside an array/list and print it.

Input Format:

First-line contains an integer number of lines to be read.

Output Format:

Print the list

Sample Input 0:

3
Sample Output 0:

['1 First line\n', '2 Second line\n', '3 Third line\n']
"""

fname = 'uploads/File-handling/Read-lines/test.txt'
# write your code here
inp = int(input())
fd = open(fname,"r")
list = fd.readlines()
sub_list =[]
for i in range(inp):
	sub_list.append(list[i])
	
print(sub_list)
	
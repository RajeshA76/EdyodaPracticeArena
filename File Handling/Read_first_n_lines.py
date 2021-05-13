"""
You will be given a file name in code editor itself and number of lines (n) you have to read first n line from given file and print it.

Input Format:

First line containes an integer number of line to be read.

Output Format:

Print that lines.

Sample Input 0:

3
Sample Output 0:

1
2
3
"""


fname = 'uploads/File-handling/Read-first-n-lines/test.txt'
# write your code here
inp = int(input())
fd = open(fname,"r")
for i in range(inp):
	print(fd.readline(),end="")
fd.close()
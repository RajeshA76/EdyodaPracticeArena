"""
You will be given a file name in the code editor itself and the number of line (n) you have to find the longest word n the given line number and print that number it there are two words with max length then print both in a new line.

Input Format:

First-line contains an integer number of lines to be read.

Output Format:

Print the word

Sample Input 0:

3
Sample Output 0:

Third
lines
"""

fname = 'uploads/File-handling/Find-longest-word/test.txt'
# write your code here
fd = open(fname,'r')
f = fd.read().splitlines()
inp = int(input())
res = f[inp-1].split()
if len(res[1]) == len(res[2]):
	print(res[1])
	print(res[2])
elif len(res[1]) > len(res[2]):
	print(res[1])
else:
	print(res[2])
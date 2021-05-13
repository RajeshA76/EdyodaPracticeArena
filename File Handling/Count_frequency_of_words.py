"""
You will be given a file name in the code editor itself You have to find the frequency of words in that file and print a dictionary of that.

Input Format:

First-line contains an integer number of lines to be read.

Output Format:

Print the dictionary

Sample Output 0:

{'1': 1, 'First': 1, 'line': 6, '2': 1, 'Second': 1, '3': 1, 'Third': 1, 'lines': 1, '4': 1, 'Fourth': 1, '5': 1, 'Fifth': 1, '6': 1, 'Sixth': 1, '7': 1, 'Seventh': 1, '80': 1, 'Number': 1, 'eigthty': 1}     
"""

fname = 'uploads/File-handling/Count-frequency-of-words/test.txt'
# write your code here
fd = open(fname,"r")
s = fd.read().split()
dict = {}
for i in range(len(s)):
	count = 0
	for j in range(len(s)):
		if s[i] == s[j]:
			count += 1
	dict[s[i]] = count
print(dict)
		
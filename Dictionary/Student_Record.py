"""
Given n names and phone numbers, assemble a students record that maps student's names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.

Note: Your student Rrecord should be a Dictionary data structure.

Input Format

The first line contains an integer, n, denoting the number of entries in the student record.
Each of the n subsequent lines describes an entry in the form of I2 space-separated values on a single line. The first value is a student's name, and the second value is an 10-digit phone number.

After the n lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.

Output Format

On a new line for each query, print Not found if the name has no corresponding entry in the student record; otherwise, print the full  Iname and phone number in the format name=phoneNumber.

Sample Input

3
david 9991222222
sam 1112222222
tom 12299933
david
edward
tom
Sample Output

david=9991222222
Not found
tom=1229993333
Explanation

We add the following (Key,Value) pairs to our dictionary so it looks like this:

studetnRecord = {'david':9991222222,'sam':1112222222,'tom':1229993333}

We then process each query and print key=value if the queried  is found in the dictionary; otherwise, we print Not found.

Query 0: david
Sam is one of the keys in our dictionary, so we print daivd=99912222.

Query 1: edward
Edward is not one of the keys in our dictionary, so we print Not found.

Query 2: tom
Harry is one of the keys in our dictionary, so we print tom=12299933.
"""


# Write your code here use STDIN for inout and STDOUT for output
n = int(input())
dict = {}

for i in range(n):
	inp = input().split()
	dict[inp[0]] = inp[1]
	
# enter name in order to get phone number
while True:
	name = input()
	if name in dict.keys():
		print("{0}={1}".format(name,dict[name]))
	elif(name == ''):
		break
	else:
		print("Not found")
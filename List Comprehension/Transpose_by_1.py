"""
Given a sentence, return the setence will all it's letter transposed by 1 in the alphabet, but only if the letter is a-y.
Input Format:

input_string containing the sentence

Output Format:

string with transposed input_string

Sample Input 0:

the quick brown fox jumps over the lazy dog
Sample Output 0:

uif rvjdl cspxo gpy kvnqt pwfs uif mbz eph
"""

input_string = input()
# Write your code here
ascii = []
transpose = []
for i in input_string:
	ascii.append(ord(i))
for i in ascii:
	if i == 32:
		transpose.append(i)
	elif i == ord('z'):
		pass
	else:
		transpose.append(i+1)
	
		
res = [chr(i) for i in transpose]
out = "".join(res)
print(out)
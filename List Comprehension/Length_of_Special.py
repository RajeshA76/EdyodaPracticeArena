"""
Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.
Input Format:

input_string containing the string

Output Format:

list containing the length of words as described in description

Sample Input 0:

the quick brown fox jumps over the lazy dog
Sample Output 0:

[5, 5, 3, 5, 4, 4, 3]
"""

input_string = input()
# Write your code here
input_list = input_string.split(" ")
list_length = []

while ("the" in input_list):
	input_list.remove("the")
for i in input_list:
	list_length.append(len(i))
print(list_length)
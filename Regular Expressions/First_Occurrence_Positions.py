"""
Write a program to capture the first occurence of an number in a string using re module
enlightened Theory:
# re.search(regX,input_string).start() will give the index of the starting of the match.
# re.search(regX,input_string).end() will give the first position where that match is not present or 1+ (the position where the match becomes over)

Input Format:

input_string will be given

Output Format:

two integers representing the start in the first line and end+1 in the second line.

Sample Input 0:

abcd12efgh13ijkl
Sample Output 0:

4
6
Explaination: First Occurence is 12, Also these are index positions. 
"""

import re
input_string = input()
# Write your code here
pattern = "\d+"
match = re.search(pattern,input_string)
print(match.start())
print(match.end())

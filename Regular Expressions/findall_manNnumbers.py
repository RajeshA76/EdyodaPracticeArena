"""
# Write an re code to print the list containing all the matching patterns from the given string based on the following pattern:
=> 3 small letter alphabets followed by 2 number between 0-9

Input Format:

input_string

Output Format:

list containing patterns matched from left to right in the string.

Sample Input 0:

man99woman99alexander345
Sample Output 0:

['man99', 'man99', 'der34']
"""


import re
input_string = input()
# Write your code here
match = re.findall("[a-z]{3}[0-9]{2}",input_string)
print(match)
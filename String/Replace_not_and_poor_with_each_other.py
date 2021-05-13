"""
You will be given a string. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'poor' follows the 'not', replace the whole 'not'...'poor' substring with 'good' else swap 'not' and 'poor'. Return the resulting string.

Input Format:

only one line contains string

Output Format:

Print the result will be a string

Sample Input 0:

The lyrics is not that poor! The lyrics is poor!
Sample Output 0:

The lyrics is good! The lyrics is poor!
"""

s = input()
# Write your code here
snot = s.find('not')
spoor = s.find('poor')
if spoor > snot and snot>0 and spoor>0:
    str1 = s.replace(s[snot:(spoor+4)], 'good')
    print(str1)
elif spoor < snot:
    str1 = s.replace(s[snot:(snot+3)],'poor')
    str2 = str1.replace(str1[spoor:(spoor+4)],'not',1)
    print(str2)
else:
    print(s)
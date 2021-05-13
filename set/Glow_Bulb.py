"""
If the ASCII value of the uncommon character between the two string is odd print odd, and if even print even.

Note: Only 1 character will be uncommon in the given_strings

Input Format:

string1 and string2

Output Format:

odd or even based on description

Sample Input 0:

bulbisglowing
bulbisnotglowing
Sample Output 0:

even
Explaination:

 Uncommon element: t

ASCII value:116 => EVEN
"""


string1 = input()
string2 = input()
# Write your code here
set1 = set(string1)
set2 = set(string2)
not_equal = set1.symmetric_difference(set2)
list = list(not_equal)
result = ord(list[0])
if result % 2 == 0:
	print("even")
else:
	print("odd")
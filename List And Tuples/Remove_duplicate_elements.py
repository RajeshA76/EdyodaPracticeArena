"""
You will be given a string having space seprated elements you have to make a list from that given string. then remove duplicates elements and print the new list.

Input Format:

one line containing string having sapce separated elements of list.

Output Format:

Print out the list wihtout havung duplicates.

Sample Input 0:

adda padda adda 123 321 123

Sample Output 0:

adda padda 123 321
"""

element = input()
# Write your code here
lis = element.split(" ")
unique = []
for i in lis:
	if i not in unique:
		unique.append(i)
print(unique)

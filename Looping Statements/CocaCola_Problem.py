"""
Write a Python program which iterates the integers from x to y.(both inclusive) For multiples of three print "Coca" instead of the number and for the multiples of five print "Cola". For numbers which are multiples of both three and five print "CocaCola".

Input Format:

Two line separated numbers x and y.

Output Format:

Output including numbers and Coca,Cola and CocaCola as discussed in the description.

Input Sample:

1
15
Output Sample:

Coca
Cola
Coca
Coca
Cola
Coca
CocaCola
 Note: Remember to change type of string to int after input()
"""

x = input()
y = input()
# Write your code here
for i in range(int(x),int(y)+1):
	if i % 3 == 0 and i % 5 == 0:
		print("CocaCola")
	elif i % 3 == 0:
		print("Coca")
	elif i % 5 == 0:
		print("Cola")
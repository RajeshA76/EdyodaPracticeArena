"""
String will be given to you. You have to calculate lions and zebra from it as follows:-

=>If ASCII value of char is even, it is a lion

=>If ASCII value of char is odd, it is a zebra

## Remember if a character repeats, it does not mean it is a different animal.

If lions are great in number, print the number of extra lions.

If zebras are great in number, print the number of extra zebras.

If zebras equal to lions print zebleo

Input Format:
string named as zoo

Output Format:

extra lions,extra zebras or zebleo based on above description

Sample Input 0:

grass
Sample Output 0:

2 zebras
"""

zoo = input()
# Write your code here
l = []
for i in zoo:
	l.append(ord(i))
set_l = set(l)
dict = {}
lion_count = 0
zebra_count = 0
for i in set_l:
	if i % 2 == 0:
		lion_count += 1
	else:
		zebra_count += 1
		
dict["lion"] = lion_count
dict["zebra"] = zebra_count
		
if dict["lion"] > dict["zebra"]:
	res = dict['lion'] - dict['zebra']
	print(res,"lions")
elif dict["zebra"] > dict["lion"]:
	res = dict['zebra'] - dict['lion']
	print(res,"zebras")
else:
	print("zebleo")
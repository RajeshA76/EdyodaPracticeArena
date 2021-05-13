#Question:
"""A shop will give a discount of 10% max up to 200rs if the cost of purchased items is more than 999rs.

Ask the user for quantity of items and consider price of each item is 150rs. Judge and print total cost for the user.

Input Format:

The first line contains an integer no of items

Output Format:

It will contain an integer value. Print the total cost to use user after discount (If applicable) it .

Sample Input 0:

10
Sample Output :

1350

"""
#Solution:

items = int(input())
# Write your code here
cost = items * 150
if cost > 999:
	discount = cost * 0.10
	if discount <= 200:
		print(int(cost - discount))
	else:
		discount = 200
		print(int(cost - discount))
else:
	print(cost)
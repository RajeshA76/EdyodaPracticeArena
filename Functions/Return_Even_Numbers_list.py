"""
Incomplete code is provided to you. Complete the function and than call it by passing the given_list.

Complete the function means:

=> return a sorted list of even numbers from the given_list

Input Format:

No need to take input, Pass the given_list while calling the function.

Output Format:

return the list containing only even numbers in sorted order.

Sample Input 0:

[1,2,3,4,5,6]
Sample Output 0:

[2, 4, 6]
"""

given_list = eval(input())
list = []
def find_even(given_list):
    # Write your code here
	for i in given_list:
		if i % 2 == 0:
			list.append(i)
	print(list)

find_even(given_list)
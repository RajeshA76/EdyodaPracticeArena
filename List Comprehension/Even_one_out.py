"""
Given a list of numbers, write a list comprehension that produces a list of only the even numbers in that list.
Input Format:

input_list containing integers.

Output Format:

print a list containing only even from the input_list

Sample Input 0:

[1,2,3,4,5]
Sample Output 0:

[2, 4]
"""

input_list = eval(input())
# Write your code here
list = [i for i in input_list if i % 2 == 0]
print(list)
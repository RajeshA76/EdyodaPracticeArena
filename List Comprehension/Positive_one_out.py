"""
Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.
Input Format:

input_list containing integers

Output Format:

list containing only positive numbers

Sample Input 0:

 [-2, -1, 0, 1, 2]
Sample Output 0:

[1, 2]
"""

input_list = eval(input())
# Write your code here
positive = [i for i in input_list if i > 0]
print(positive)
"""
Given a list of numbers, write a list comprehension that produces a list of each number doubled
Input Format:

input_list will be given

Output Format:

list with required change as in description

Sample Input 0:

[1, 2, 3, 4, 5]
Sample Output 0:

[2, 4, 6, 8, 10]
"""

input_list = eval(input())
# Write your code here
a = list([(2*i) for i in input_list])
print(a)

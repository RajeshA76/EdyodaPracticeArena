"""
Given a list of numbers, write a list comprehension that produces a list of strings of each number that is divisible by 5.
Input Format:

input_list will be given containing integers

Output Format:

list containing only multiple of 5

Sample Input 0:

[25, 91, 22, -7, -20]
Sample Output 0:

 ['25', '-20']
"""
input_list = eval(input())
# Write your code here
result = [i for i in input_list if i % 5 == 0]
print(result)

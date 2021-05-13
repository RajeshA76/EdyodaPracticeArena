"""
Given a list of number, return the list with all even numbers doubled, and all odd numbers turned negative
Input Format:

given_list containing integers

Output Format:

list with integers turned as prescribed in the description.

Sample Input 0:

[-5,-2,1,0,5,9,7,8,3,4]
Sample Output 0:

[5, -4, -1, 0, -5, -9, -7, 16, -3, 8]
"""

given_list = eval(input())
# Write your code here
result = [i*2 if i % 2 == 0 else -i for i in given_list]
print(result)
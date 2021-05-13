"""
 Write a Python program to filter a given list of whether the values in the list are having a length of 6 using Lambda
Input Format:

input_list containing words

Output Format:

Print the list containing only 6 length words

Sample Input 0:

Monday Tuesday Wednesday Thursday Friday Saturday Sunday
Sample Output 0:

['Monday', 'Friday', 'Sunday']
"""

input_list = list(map(str,input().split())) # readonly
x = lambda input_list : [i for i in input_list if len(i)==6]
print(x(input_list))
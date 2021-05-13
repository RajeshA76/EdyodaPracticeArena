"""
.Write a Python program to add two given lists using map and lambda
Input Format:

input_list_1 and input_list_2 are provided with integers

Output Format:

final_list which contaings sum of elements one by one.

Sample Input 0:

1 2 3
2 3 4
Sample Output 0:

[3, 5, 7]
"""

input_list_1 = map(int,input().split()) # readonly
input_list_2 = map(int,input().split()) # readonly
final_list = list(map(lambda x,y: x+y,input_list_1,input_list_2))# Complete this code using lambda))
print(final_list)# readonly

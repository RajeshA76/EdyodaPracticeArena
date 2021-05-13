"""
Two list will be given to you , Find the Intersection points between two list and print them in sorted order.

Input Format:

Two list input_list_1 and input_list_2

Output Format:

output_list containing the intersection elements in sorted Order.

Sample Input 0:

1 2 3 5 7 8 9 10
1 2 4 8 9
Sample Output 0:

[1, 2, 8, 9]
"""

input_list_1 = list(map(int,input().split())) #readonly
input_list_2 = list(map(int,input().split())) #readonly
x = lambda input_list_1, input_list_2 : sorted(list(set(input_list_1).intersection(set(input_list_2))))
print(x(input_list_1,input_list_2))
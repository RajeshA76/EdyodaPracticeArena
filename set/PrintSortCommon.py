"""
Print the sorted common elements between the given set.

Input Format:

set_1 and set_2

Output Format:

sorted list of common elements

Sample Input 0:

12 23 34 45 56
34 45 12 89
Sample Output 0:

['12', '34', '45']
"""

set_1 = set(input().split())
set_2 = set(input().split())
# Write your code here
list_set = list(set_1.intersection(set_2))
print(sorted(list_set))
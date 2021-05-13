"""
Print the length of Uncommon elements between two sets.

Input Format:

set_1 and set_2

Output Format:

Print the length of the Uncommon elements between the two.

Sample Input 0:

12 23 34 45 56
34 45 78 90 100
Sample Output 0:

['100', '12', '23', '56', '78', '90']
"""

set_1 = set(input().split())
set_2 = set(input().split())
# Write your code here
set_3 = set_1.symmetric_difference(set_2)
l = sorted(list(set_3))
print(l)
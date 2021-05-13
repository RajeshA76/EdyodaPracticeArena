"""
2 list will be given, first_list and second_list.

=> If first list is subset of second_list, print the sorted list of non-common elements between the two list.

=> If the first list is not subset of second list, print "No"

Input Format:

No need to take input, first_list and second_list is provided to you.

Output Format:

Print the sorted list of non-common elements or "No"

Sample Input 0:

[1,2,3],[5,1,3,4,2]
Sample Output 0:

[4,5]
Sample Input 1:

[5,1,3,4,2],[1,2,3]
Sample Output 1:

No
"""


first_list,second_list = eval(input())
# Write your code here
set1,set2 = set(first_list),set(second_list)
if set1.issubset(set2):
	print(sorted(list(set1.symmetric_difference(set2))))
else:
	print("No")
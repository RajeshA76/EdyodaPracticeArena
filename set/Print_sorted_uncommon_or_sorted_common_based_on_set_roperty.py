"""
2 list will be given, first_list and second_list.

=> If first list is subset of second_list, print the sorted list of non-common elements between the two list.

=> If the first list is not subset of second list, print the sorted common even elements between the two list.

Input Format:

No need to take input, first_list and second_list is provided to you.

Output Format:

Print the sorted list of non-common elements or sorted list of common as explained above.

Sample Input 0:

[5,1,3,4,2,6,8],[1,2,3,8,6]
Sample Output 0:

[2, 6, 8]
Sample Input 1:

[1,2,3],[5,1,3,4,2]
 Sample Output 1:

[4, 5]
"""

first_list,second_list = eval(input())
# Write your code here
s1,s2 = set(first_list),set(second_list)
if s1.issubset(s2):
	print(list(sorted(s1.symmetric_difference(s2))))
else:
	res = list(sorted(s1.intersection(s2)))
	even_list = []
	for i in res:
		if i % 2 == 0:
			even_list.append(i)
	print(even_list)
			
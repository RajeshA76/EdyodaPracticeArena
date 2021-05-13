"""
You will be given a list. You have to print a list whose 1st element should largest and 2nd should be smallest then 3rd should be 2nd largest and 4th should be 2nd smallest and so on.

Input Format:

First line will have space separated elements of list.

Output Format:

Print the reuired list.

Sample Input 0:

1 2 3 4 5 6

Sample Output 0:

6 1 5 2 4 3
"""
l = list(map(int, input().split()))
# Write your code here
new_list = []
for i in range(len(l)):
	if i % 2 == 0:
		new_list.append(max(l))
		l.remove(max(l))
	else:
		new_list.append(min(l))
		l.remove(min(l))
						
print(new_list)

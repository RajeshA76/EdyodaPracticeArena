"""
You will be given a total number of element initially and in next line containing tuple's elements. so first creat a tuple from the given string. Then you have to add a given element at given index value.

Input Format:

The first line contains intefger (a total number of element initially) and in next n line containing space separated tuple's elements. In last line it will have index value and element followed by space.

Output Format:

Final tuple after adding given element

Sample Input 0:

5
abda
defd
123
Edyoda
Saas
3 Three
Sample Output 0:

('abda', 'defd', '123', 'Three', 'Edyoda', 'Saas')
"""

n = int(input())
# Write your code here
lis = []
for i in range(n):
	inp = input()
	lis.append(inp)	
add_value = input()
list_split = add_value.split(" ")
lis.insert(int(list_split[0]),str(list_split[1]))
your_answer = tuple(lis)
print(your_answer)

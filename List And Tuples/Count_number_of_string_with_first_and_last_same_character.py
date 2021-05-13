"""
You will have number or elements and next n lines containing list elements. You have to create list from that given string. Write a program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.¶

Input Format:

In first-line it will have an integer (numbers of elements inside a list). In the second line, it will have a list elements separated by space.

Output Format:

One line containing integer (count as per given condition)

Sample Input 0:

5
abda
defd
123
Edyoda
Saas
Sample Output 0:

2
"""
n = int(input())
# Write your code here
your_answer = 0
for i in range(n):
	inp = input()
	if inp[0] == inp[-1]:
		your_answer += 1

print(your_answer)

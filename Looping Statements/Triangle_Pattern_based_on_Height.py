"""
Write a Python program to print a triange based on the height given, using a nested for loop. For example for height = 5

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

Input Format:

height from the input

Output Format:

print the pattern with the given height.

Sample Input 0:

3
Sample Output 0:

*
* *
* * *
* *
*

"""

n = int(input())
# Write your code here use STDIN for inout and STDOUT for output
out = '* '
for i in range(1,n+1):
	print(out * i)
for i in range(n-1,0,-1):
	print(out * i)
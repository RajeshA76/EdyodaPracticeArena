"""
 Write a program to print a new number with digits reversed as of orignal one. The number provided will be greater than or equal to 0

Input Format:
Input Integer in variable n

Output Format:
print the reverse of the number n.

Sample Input 0:
1234
 
Sample Output 0:
4321
"""

n = int(input())
# Write your code here use STDIN for inout and STDOUT for output
string = str(n)[::-1]
print(int(string))
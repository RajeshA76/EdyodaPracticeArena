#Question 
"""
A company decided to deduct pf of 12% of salary if year of service is less than or equal to 5 year and 24% employee if his/her year of service is more than 5 years.
Ask the user for their salary and year of service and print the net in-hand salary after pf deduction.
 
Input Format:
There will be two lines first line will be containing a single integer(Salary) and second will contain single integer (no of years).
 
Output Format:
There will be one line containing a integer number(In-hand salary).
 
Sample Input 0:
10000
2
 
Sample Output 0:
8800
"""
#Solution:


sal = int(input())
noy = int(input())
# Write your code here
if (noy >= 0 and noy <= 5):
	deduct = sal - sal * 0.12
if (noy > 5):
	deduct = sal - sal * 0.24
	

print(int(deduct))
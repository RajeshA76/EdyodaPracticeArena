#Question
"""
You will be given an integer it would be year number E.G. 2020 You have to find out is it leap year or not?

Rules to define a leap year:

If a year is divisible by 4 then it is a leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

Input Format:

The first line contains integer Year number

Output Format:

Print "True" or "False" without quotes.

Sample Input 0:

2020
Sample Output :

True
"""
#Solution:

year = int(input())
# Write your code here
if year % 4 == 0:
	if year % 400 == 0 and year % 100 != 0:
		is_leap_year = "True"
	elif year % 400 != 0 and year % 100 == 0:
		is_leap_year = "False"
	else:
		is_leap_year = "True"
else:
	is_leap_year = "False"



print(is_leap_year)


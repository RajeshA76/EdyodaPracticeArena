"""
Write a program with regular expression to achieve the following objective:

A string with date inside is given. Date is precedded by / and succedded by /. Like:

edyoda/assessment/1947/08/14/

Write this in this format: ddmmmyyyy

Here mmm is taken from the month_dict corresponding to the month.

14Aug1947
Input Format:

input_string and month_dict will be provided

Output Format:

Date in the required fomat as in description

Sample Input 0:

edyoda/assessment/1947/08/14/
Sample Output 0:

14Aug1947
"""

import re
input_string = input()
month_dict = {"01":"Jan","02":"Feb","03":"Mar","04":"Apr","05":"May","06":"Jun","07":"Jul","08":"Aug","09":"Sep",
              "10":"Oct","11":"Nov","12":"Dec"}
# Write your code here
match = re.search("\d{4}\/\d{2}\/\d{2}",input_string)
l = match.group().split("/")
print("{}{}{}".format(l[2],month_dict[l[1]],l[0]))

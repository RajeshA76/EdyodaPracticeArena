"""
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

Input Format:

Input_String variable will contain the input.

Output Format:

Output a dictionary containing {'UPPER_CASE': n1, 'LOWER_CASE': n2} .  here n1 and n2 are integers for respective counts.

Sample Input 0:

Apple123
Sample Output 0:

{'UPPER_CASE': 1, 'LOWER_CASE': 4}

"""

Input_String = input()

def find_upper_lower(Input):
# Write your code here
	LOWER_CASE = 0
	UPPER_CASE = 0
	for i in Input:
		if i.islower():
			LOWER_CASE += 1
		elif i.isupper():
			UPPER_CASE += 1
	dict = {'UPPER_CASE':UPPER_CASE,'LOWER_CASE':LOWER_CASE}
	return(dict)
		
	
	
print(find_upper_lower(Input_String))
"""
Write a Python function that checks whether a passed string is palindrome or not.

Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nursesrun.

Input Format:

Input_String containing String to be tested if palindrome or not

Output Format:

palindrome or not palindome as given in the description

Sample Input 0:

madam
Sample Output 0:

palindrome
Sample Input 1:

edyoda
Sample Output 1:

not palindrome
"""



Input_String = input()

def check_palindrome(Input_String):
# Write your code here
	if Input_String[:] == Input_String[::-1]:
		return "palindrome"
	else:
		return "not palindrome"
	
print(check_palindrome(Input_String))
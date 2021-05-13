"""
Write a Python program to find palindromes in a given list of strings using Lambda and filter.

A palindromic number or numeral palindrome is a number that remains the same when its digits are reversed. Like 16461, for example, it is "symmetrical".
Similarly for words.

Input Format:

input_list containing words

Output Format:

final_list containing only words which are palindrome

Sample Input 0:

php w3r Python abcd Java aaa
Sample Output 0:

['php', 'aaa']
"""

input_list = list(map(str,input().split()))
final_list = list(filter(lambda x:x[:]==x[::-1],input_list))# Use lambda and filter to complete this code)
print(final_list)

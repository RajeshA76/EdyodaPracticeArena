"""
Write a Python program to find all anagrams of a string in a given list of strings using lambda.
An anagram is a direct word switch or wordplay, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; for example, the word anagram can be rearranged into nag-a-ram.

Your task is to write the whole code including taking input from the user.

Input Format:

2 lines will be there. First line containing the strings space separated. Second line the target string whose anagrams needs to be found 

on the list given on First line.

Output Format:

Print the list containing only the anagrams from the above list.

Sample Input 0:

bcda abce cbda cbea adcb 
abcd
Sample Output 0:

['bcda', 'cbda', 'adcb']
"""

#Write the whole code including taking input using map,etc
from collections import Counter
input_list = input().split()
anagram = input()
len_list = [i for i in range(len(anagram))]

anon_fun = list(filter(lambda x:Counter(x) == Counter(anagram),input_list))
print(anon_fun)
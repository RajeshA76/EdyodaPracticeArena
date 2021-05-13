"""
Given a string representing a word, write a set comprehension that produces a set of all the vowels in that word. Output should than 
be converted to a sorted list.

Input Format:

input_word containing the word.

Output Format:

list containing all the unique vowels in sorted order

Sample Input 0:

mathematics
Sample Output 0:

['a', 'e', 'i']
"""

input_word = input()
# Write your code here
res = set([i for i in input_word if i in 'aeiou'])
print(sorted(list(res)))

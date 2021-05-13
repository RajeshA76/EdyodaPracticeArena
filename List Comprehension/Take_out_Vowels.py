"""
Given a string representing a word, write a list comprehension that produces a list of all the vowels in that word in sorted order.
Input Format:

input_word containing the word.

Output Format:

list containing all the vowels in sorted order

Sample Input 0:

mathematics
Sample Output 0:

['a', 'a', 'e', 'i']
"""


input_word = input()
# Write your code here
vowels = 'aeiou'
res = sorted([i for i in input_word if i in vowels])
print(res)
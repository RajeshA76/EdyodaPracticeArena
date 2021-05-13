"""
Given a sentence, return the sentence with all vowels removed.
Input Format:

input_string containing a sentence

Output Format:

string without the vowels from input_string

Sample Input 0:

the quick brown fox jumps over the lazy dog
Sample Output 0:

th qck brwn fx jmps vr th lzy dg
"""


input_string = input()
# Write your code here
res = [i for i in input_string if i not in 'aeiou']
print("".join(res))
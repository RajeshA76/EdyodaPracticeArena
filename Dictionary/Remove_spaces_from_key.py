"""
You will be given an integer(n) number key-value pair and in next n lines you will be given comma seprated key value. you have to create a dictionary from that given strings after removing spaces from key.

Input Format:

The Frist line contains integer n and for next n line contiang comma seprated key-values pair. in last it will contain that key value to be added in exiting dictionary.

Output Format:

Print the dictionary

Sample Input 0:

2
S 001, 'Math'
S   002, 'English'
Sample Output 0:

{'S001':'Math','S002':'English'}
"""

n = int(input())
# Write your code here
dict ={}
for val in range(n):
    d,d1 = input().split(",")
    s = d.replace(" ","")
    dict[s] = d1
print(dict)
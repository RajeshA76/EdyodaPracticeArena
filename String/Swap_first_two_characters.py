"""
You will be given two strings.you have to get a new string from two given strings, separate by space, and swap the first two characters of each string.

Input Format:

Two lines containing a string in each.

Output Format:

Print the new string.

Sample Input 0:

Edyoda
123
Sample Output 0:

12yoda Ed3
"""

s1 = input()
s2 = input()
# Write your code here
s1_list = [i for i in s1]
s2_list = [i for i in s2]
[s1_list[0:2],s2_list[0:2]] = [s2_list[0:2],s1_list[0:2]]
join_s1 = ''.join(s1_list)
join_s2 = ''.join(s2_list)
print(join_s1,join_s2)
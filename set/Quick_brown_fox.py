"""
Print Yes if the given_set contains all the alphabets, else print the number of missing alphabets.

Like "Yes" if all alphabets are present in string "the quick brown fox jumps over a lazy dog" or length like for given string "lazy" output 22

Input Format:

No need to take input, take given_set

Output Format:

"Yes" or Length as explained above.

Sample Input 0:

lazy
Sample Output 0:

22
Sample Input 1:

the quick brown fox jumps over a lazy dog
Sample Output 1:

Yes 
"""

given_set = set(input())
# Write your code here
list_set = list(given_set)
list_alphabets = [chr(i) for i in range(97,123)]
l1 = []
for i in list_set:
	if i in list_alphabets:
		l1.append(i)
		
		
if len(l1) == 26:
	print("Yes")
else:
	print(len(list_alphabets) - len(l1))
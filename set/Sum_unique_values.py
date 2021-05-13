"""
Print sum of the unique values of the given dictionary. 

Input Format:

given_dict will be given

Output Format:

sum of the unique values

Sample Input 0:

{"python":3,"django":2,"java":8,"numpy":1,"pandas":1}
Sample Output 0:

14
"""

given_dict = eval(input())
# Write your code here
dict_set = set(given_dict.values())
sum = 0
for i in dict_set:
	sum = sum + i
	
print(sum)
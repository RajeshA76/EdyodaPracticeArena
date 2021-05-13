"""
You will have a dictionary here. You have to swap key values of the dictionary.
 
For example: input_dictionary = {'A':1, 'B':2} so your output_dictionary should be {1:'A', 2:'B'}
But again here is a twist if we have multiple keys with the same values i.e. (‘A’, 1) and (‘D’, 1) then the output should be {1:['A', 'D']}.
 
Input Format:
In first-line it will have an integer. In the second line, it will have a key-value separated by space.
 
Output Format:
A single line containing dictionary.
 
Sample Input 0:
5
A 1
B 2
C 3
D 1
E 1
 
Sample Output 0:
{'1':['A','D','E'], '2':'B', '3':'C'}
"""

n = int(input())
dict ={}                     
for i in range(n):        
    text = input().split()
    dict[text[0]] = text[1]
new_dict={}
# Write your code here
for key in dict:
    if dict[key] in new_dict:
        new_dict[dict[key]].append(key)
            
    else:
        new_dict[dict[key]] = [key]

print(new_dict)
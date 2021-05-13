"""
1,2,3,4,5,6 to be returned as one,two,three,four,five,six

no. will be given, Convert into word like above..

Input Format:

No need to take input, an no. will be given, Just pass that while calling the function.

Output Format:

Print the word of that number

Sample Input 0:

1
Sample Output 0:

one
"""

no = int(input())
dict = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six"}
def change_to_word(no):
		    # Write your code here
	print(dict[no])
	
change_to_word(no)
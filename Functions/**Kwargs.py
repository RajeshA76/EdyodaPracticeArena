"""
the function task will be restricted to take only **kwargs, which you have to use to pass 3 values and print them like

given_name is studying at given_college he/she/they took the stream given_stream

here given_name,given_college and given_stream are to be used as given.

he/she/they depends upon:

he: gvien_gender = male

she: given_gender = female

they: given_gender is none of male or female

Input Format:

given_name is studying at given_college he/she/they took the stream given_stream as explained above

Output Format:

here given_name,given_college and given_stream are to be used as given.

Sample Input 0:

rohan mit computer_science
Sample Output 0:

rohan is studying at mit he took the stream computer_science
"""

given_name,given_college,given_stream,given_gender = map(str,input().split())

def task(**kwargs):
# Write your code here
	if given_gender == "male":
		print(given_name,"is studying at",given_college,"he took the stream",given_stream)
	elif given_gender == "female":
		print(given_name,"is studying at",given_college,"she took the stream",given_stream)
	else:
		print(given_name,"is studying at",given_college,"they took the stream",given_stream)
		
task(name=given_name,college=given_college,stream=given_stream,gender=given_gender)
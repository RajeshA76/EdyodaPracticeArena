"""
Call the function details dependent on the input.

Conditions:

1) If the input_name = rohan, print the default name and not this.

2) If the input_college = mit, print the default college and not this.

Input Format:

input_name,input_college and input_stream is given.

Output Format:

Call the function with proper arguments, it will give the correct output.

Sample Input 0:

rohan,mit,computer_science
Sample Output 0:

name= rohan rathore stream= computer_science college= MIT
"""


input_name,input_college,input_stream = map(str,input().split(","))
def details(stream,name="rohan rathore",college="MIT"):
    print("name=",name,"stream=",stream,"college=",college)
    
# Write your code here
if input_name == "rohan" and input_college == "mit":
	details(input_stream)
elif input_college == "mit":
	details(input_stream,name=input_name)
elif input_name == "rohan":
	details(input_stream,college=input_college)
else:
	details(input_stream,name=input_name,college=input_college)
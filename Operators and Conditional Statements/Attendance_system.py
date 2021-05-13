#Question
"""
A student will not be allowed to sit in the exam if his/her attendance is less than 75%. if he/she has medical cause reduce attendance criteria to 60%. Ask the user if he/she has a medical cause or not ( 'Y' or 'N' ) and print accordingly. You were given total no classes and total classes attended by the student.

Input Format:

The first line contains integer total_classes and the second line contains integer attended_classes and the tired line contains string medical cause Y or N.

Output Format:

Print "True" or "False" without quotes.

Sample Input 0:

250
150
N
Sample Output :

False
"""
#Solution:

total_classes = int(input())
attended_classes = int(input())
medical_cause = input()
# Write your code here
if medical_cause == "Y":
	if ((attended_classes / total_classes) * 100 ) >= 60:
		is_allowed = "True"
	else:
		is_allowed = "False"
elif medical_cause == "N":
	if ((attended_classes / total_classes) * 100) >= 75 :
		is_allowed = "True"
	else:
		is_allowed = "False" 
print(is_allowed)
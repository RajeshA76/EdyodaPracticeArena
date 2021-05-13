#Question
"""
A school has following rules for grading system:

   a. Below 40 - F

   b. 40 to 50 - C

   c. 50 to 60 - C+ 

   d. 60 to 70 - B 

   e. 70 to 80 - B+

   f. 80 to 90- A

   g. Above 90 - A+

Ask the user to enter marks for their 5 main subjects and print the overall grade (Be careful grades will be case sensitive) for an average of their marks.

Input Format:

There will be 5 lines containing single integer each line equivalent to mark for each subject.

Output Format:

There will be two lines first that will contain a string that will be the user's final grade and second that will contain float number (average of user's marks)

Sample Input 0:

75
95
85
90
80
Sample Output :

A
85.0
"""
#Solution:

subject1_mark = int(input())
subject2_mark = int(input())
subject3_mark = int(input())
subject4_mark = int(input())
subject5_mark = int(input())
# Write your code here
grades = ["A+","A","B+","B","C+","C+","F"]
average = (subject1_mark + subject2_mark + subject3_mark + subject4_mark + subject5_mark) / 5
if average > 90:
	print(grades[0])
elif average >= 80 and average < 90:
	print(grades[1])
elif average >= 70 and average < 80:
	print(grades[2])
elif average >= 60 and average < 70:
	print(grades[3])
elif average >= 50 and average < 60:
	print(grades[4])
elif average >= 40 and average < 50:
	print(grades[5])
else:
	print(grades[6])
	
print(average)
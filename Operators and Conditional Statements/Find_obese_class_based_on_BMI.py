#Question:
"""
Body mass index (BMI) is a value derived from the mass (weight) and height of a person. The BMI is defined as the body mass divided by the square of the body height and is universally expressed in units of kg/m2, resulting from mass in kilograms and height in meters. BMI Formula = weight / (height*height)

Write a program, which asks for the length(in meters) and the weight(in KG) of a person and returns an evaluation string according to the following table(in range right side number is exluded):

BMI Range	Result
< 15	very severely underweight
15-16	severely underweight
16-18.5	underweight
18.5-25	normal
25-30	overweight
30-35	moderately obese
35-40	severely obese
40< BMI	very severely obese
 

Input Format:

The first line contains a float number weight and the second line contains a float number height 

Output Format:

It will contain a string result as per the above table. Be careful to use the same spellings as given in result column.

Sample Input 0:

48
1.64
Sample Output :

underweight
"""
#Solution:

weight = float(input())
height = float(input())
# Write your code here
BMI = weight / (height * height)
if BMI < 15:
	print("very severely underweight")
elif BMI >= 15 and BMI < 16:
	print("severely underweight")
elif BMI >= 16 and BMI < 18.5:
	print("underweight")
elif BMI >= 18.5 and BMI < 25:
	print("normal")
elif BMI >= 25 and BMI < 30:
	print("overweight")
elif BMI >= 30 and BMI < 35:
	print("moderately obese")
elif BMI >= 35 and BMI < 40:
	print("severely obese")
else:
	print("very severly obese")
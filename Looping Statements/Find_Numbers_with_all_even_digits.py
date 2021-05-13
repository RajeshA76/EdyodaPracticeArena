"""
Write a Python program to find numbers between x and y (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

Input Format:

Space Separated Integers x and y.

Output Format:

All the numbers as above description on new lines but with an comma in the end.

Input Sample:

2 48
Output Sample:

2,
4,
6,
8,
20,
22,
24,
26,
28,
40,
42,
44,
46,
48,

"""
x,y = input().split(" ")
# Write your code here
list = [i for i in range(int(x),int(y)+1)]
result = []
for num in list:
	st = str(num)
	str_list = [int(string) for string in st]
	div_list = []
	for i in str_list:
		if i % 2 == 0:
			div_list.append(i)
	if str_list == div_list:
		result.append(str(num) + ",")
			
for i in result:
	print(i)
"""
A three digit number is called Armstrong number if sum of cube of its digit is equal to number itself.

E.g.- 153 is an Armstrong number because (1^3)+(5^3)+(3^3) = 153. Write all Armstrong numbers between 100 to 500

Find all the Armstrong number between two integers x and y.(both number inclusive)

Constraints:

x and y are 3 digits only
Input Format:

Two lines containing Positive integers x and y

Output Format:

All the Armstrong numbers one after the other in new lines.

Sample Input:

100
500
Sample Output:

153
370
371
407
"""

x = input()
y = input()
# Write your code here
for i in range(int(x),int(y) + 1):
	string_list = [str(j) for j in str(i)]
	sum = 0
	for numbers in string_list:
		sum = sum + (int(numbers) * int(numbers) * int(numbers))
		
	if sum == i:
		print(i)
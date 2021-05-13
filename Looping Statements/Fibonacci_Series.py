"""You will be given an integer. You have to fibonacci series.

Note : The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, .... Every next number is found by adding up the two numbers before it. 1st and 2nd term of a fibonacci series are : 0 and 1

Input Format:

One integer value in one line (Number or terms)

Output Format:

Print space separated terms on fibonacci series

Sample Input 0:

5
Sample Output 0:

0 1 1 2 3
"""

nterms = int(input())
# Write your code here use STDIN for inout and STDOUT for output
# Function for nth Fibonacci number
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
if nterms == 0:
	print(Fibonacci(0))
else:
	for i in range(nterms):
		print(Fibonacci(i),end=" ")
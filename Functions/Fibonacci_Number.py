"""
Find nth fibonacci number. If it starts with 0,1,1,2.....

Also Print Incorrect Input if n is less than or equal to 0.

Input Format:

Call the function with n

Output Format:

Print the nth fibonacci number

Sample Input 0:

4

Sample Output 0:

2

Sample Input 1:

0

Sample Output 1:

Incorrect input

"""

# Remember you have to call the function
n = int(input())
def Fibonacci(n):
# Write your code here
	if n == 0:
		return("Incorrect input")
	else:
		if n == 1:
			res = 0
			return(res)
		elif n == 2: 
			res = 1
			return(res)
		else:
			res = Fibonacci(n - 1) + Fibonacci(n -2)
			return(res)
			
print(Fibonacci(n))


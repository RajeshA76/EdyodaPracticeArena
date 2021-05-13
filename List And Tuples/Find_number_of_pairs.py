"""
You will be given a list and a value. You have to find all the pairs of 3 elements whose sum is equal to given value. You have to print number of such pairs.

Input Format:

first line contains space seprated elements of list and second line contains an integer (Value)

Output Format:

Print an integer number of such pairs.

Sample Input 0:

-1 0 1 5 -5 6
0
Sample Output 0:

3
"""
l = list(map(int, input().split()))
value = int(input())
# Write your code here use STDIN for inout and STDOUT for output

count = 0
for i in range(len(l) - 2):
	for j in range(i+1,len(l)):
		for k in range(j+1,len(l)):
			sum = 0
			sum = l[i] + l[j] + l[k]
			if sum == value:
				count = count + 1
				
print(count)
		
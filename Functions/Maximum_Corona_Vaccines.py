"""
Suppose Vaccine is made up of n ingredients, It will be made only if all of them are present in the prescribed quantitiy. How many maximum Vaccines can you form if Max Limit of Lab ingredients are given.

Note: Remember Half Vaccines are of no use.

Input Format:

Prescribed_quantity,Max_limit_quantity

Output Format:

Print the maximum number of vaccines formed.

Sample Input 0:

[10,20,30,40],[1,2,3,10]
Sample Output 0:

4
Explaination: Since ingredient 4th is only 40 and each vaccine requires 10. Hence Total 4 Vaccines are possible.
"""


Max_limit_quantity = list(map(int,input().split()))
Prescribed_quantity = list(map(int,input().split()))

def how_many_vaccines(Max_limit_quantity,Prescribed_quantity):
    # Write your code here
	max_vacines = []
	for i in range(len(Max_limit_quantity)):
		max_vacines.append(Max_limit_quantity[i] // Prescribed_quantity[i])
	return(min(max_vacines))
		
print(how_many_vaccines(Max_limit_quantity,Prescribed_quantity))
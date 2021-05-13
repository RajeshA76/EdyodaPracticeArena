"""
Complete the class B and make an object of B to print the name and age

Input Format:

input_name and input_age is provided, use them to create the object of Class B

Output Format:

Print the name and age in two different lines

Sample Input 0:

elon musk
49
Sample Output 0:

elon musk
49
"""

input_name = input()
input_age = int(input())
class A:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name

class B(A):
    def __init__(self,name,age):
        super().__init__(name,age)
# Write your code here
b = B(input_name,input_age)
print(b.get_name())
print(b.get_age())
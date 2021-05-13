"""
You will have to finish some of the internal functions of a class like the init method, and the addmethod and the name of a method to print the details of the object with print(obj).

Input Format:

The input will provide real and imaginary values of two complex numbers

Output Format:

Sum of the two complex numbers into a new complex number and this will be printed by a function whose name you have to decide for proper functionality

Sample Input 0:

3 4
4 5
Sample Output 0:

7+9j
"""

class Complex: #readonly
    def __init__(self,real,imaginary):#readonly
        self.real = real
        self.imaginary = imaginary
        
    def addComplex(c1,c2):#readonly
        r = c1.real.__add__(c2.real)
        i = c1.imaginary.__add__(c2.imaginary)
        return str(r) + "+" + str(i) + "j"
	
    def __repr__(self):
        return str(self.real)+"+"+str(self.imaginary)+"j" #readonly
        
obj1_values = tuple(map(int,input().split()))#readonly
obj2_values = tuple(map(int,input().split()))#readonly
obj1 = Complex(*obj1_values)#readonly
obj2 = Complex(*obj2_values)#readonly

obj3 = obj1.addComplex(obj2)#readonly
print(obj3)#readonly

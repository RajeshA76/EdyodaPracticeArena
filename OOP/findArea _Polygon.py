"""
Complete the init and findArea function of the classess given.We match only integer converted area. So, Remember to typecast area into integer using int().

Input Format:

Input will be taken by the inputSides function. Complete te init somehow to use that existing functionality of polygons.

Output Format:

Output will be printed by the findArea function

Sample Input 0:

1 2 3
2 4 2 4
Sample Output 0:

0
8
"""

class Polygon:#readonly
    def __init__(self, no_of_sides):#readonly
        self.n = no_of_sides#readonly
        self.sides = [0 for i in range(no_of_sides)]#readonly

    def inputSides(self):#readonly
        self.sides = list(map(int,input().split()))#readonly
            
class Triangle(Polygon):#readonly
    def __init__(self):#readonly
        Polygon.__init__(self,3)

    def findArea(self):#readonly
        a,b,c = self.sides
        s = (a + b + c)/2
        area = (s * (s -a) * (s - b) * (s-c) ) ** 0.5
        print(int(area))
                
        
class Rectangle(Polygon):#readonly
    def __init__(self):
        Polygon.__init__(self,4)
        
    def findArea(self):#readonly
        a,b,c,d = self.sides
        area = a * b
        print(area)
        
obj1 = Triangle() #readonly
obj2 = Rectangle() #readonly
obj1.inputSides()
obj2.inputSides()
obj1.findArea()#readonly
obj2.findArea()#readonly

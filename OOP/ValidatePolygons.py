"""
Your task is to complete the validate_triangle and validate_rectangle functions for the classes.Hint for validating is given in the

comments of the code. Also you will have to print the following after validation in respective functions:-

1.Invalid Triangle: If the triangle sum property of sides is not valid(More hint in the comments of code)

2.Valid Triangle:If the triangle sum property of sides is valid.

3.Valid Rectangle:If 2 side pairs are same and they are input in correct order like l,b,l,b

4.Invalid Rectangle: If Not Valid rectangle as stated above.

Input Format:

The side length of triangle followed by for rectangle in the next line in order.

Output Format:

since object are created in order, so first validate info about triangle will come and than rectangle.

Sample Input 0:

3 4 5
2 4 2 4
Sample Output 0:

Valid Triangle
Valid Rectangle
"""

class Polygon:#readonly
    def __init__(self, no_of_sides):#readonly
        self.n = no_of_sides#readonly
        self.sides = [0 for i in range(no_of_sides)]#readonly

    def inputSides(self):#readonly
        self.sides = list(map(int,input().split()))#readonly


class Triangle(Polygon):#readonly
    def __init__(self):#readonly
        Polygon.__init__(self,3)#readonly
        
    def validate_triangle(self):#readonly
        a,b,c = self.sides
        if (a + b) > c and (a + c) > b and (b + c) > a:
            print("Valid Triangle")
        else:
            print("Invalid Triangle")
		# The sum of the lengths of any two sides of a triangle is greater than the length of the third side.
        # Use this to validate triangle on sides.

                
        
class Rectangle(Polygon):#readonly
    def __init__(self):#readonly
        Polygon.__init__(self,4)#readonly
        
    def validate_rectangle(self):#readonly
        a,b,c,d = self.sides
        if a == c:
            if b == d:
                print("Valid Rectangle")
            else:
                print("Invalid Rectangle")
        else:
            print("Invalid Rectangle")
		# Always the value in sides list will be l,b,l,b order.
        # So opposite pairs should have same values.
        # Use this to validate traingle on sides
        
obj1 = Triangle()#readonly
obj1.inputSides()#readonly
obj2 = Rectangle()#readonly
obj2.inputSides()#readonly

obj1.validate_triangle()#readonly
obj2.validate_rectangle()#readonly
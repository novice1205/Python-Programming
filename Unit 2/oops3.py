# Method Resolution Order (MRO)
import math
class Shape:
    def __init__(self,sides):
        self.sides = sides
    def __str__(self):
        return f"Shape with {self.sides} sides"
    
class Polygon(Shape):
    def area(self):
        print("Area is not calculated")

class Triangle(Polygon):
    def __init__(self,side,s_length):
        super().__init__(side)
        self.s_length = s_length
        
    def area(self):
        return (self.s_length**2*math.sqrt(3))/4

class Square(Polygon):
    def __init__(self,side,s_length):
        super().__init__(side)
        self.s_length = s_length
        
    def area(self):
        return self.s_length ** 2
    
    
print(Triangle.mro())
print(Square.mro())


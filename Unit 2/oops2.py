#MultiLevel Inheritance
import math
class Shape:
    def __init__(self,color):
        self.color = color
class Polygon(Shape):
    def __init(self,color,sides):
        super().__init__(color)
        self.sides = sides
class Triangle(Polygon):
    def __init__(self, sides, s_length):
        super().__init__(sides)
        self.s_length = s_length
    def area(self):
        return (self.s_length**2*math.sqrt(3))/4

tri = Triangle(3,5)
print("The shape is a triangle having " + tri.color + "and" + str(tri.sides) + "sides of" + str(tri.s_length) + " length") 
print(tri.area())
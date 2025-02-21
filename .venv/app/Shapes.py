import math

class Circle:
    def __init__(self, r:float):
        self.radius = r

    def area(self)->float:
        return (self.radius**2)*math.pi

    def perimeter(self)->float:
        return self.radius*2*math.pi

    def __str__(self):
        return f"Circle with a radius of {self.radius}\nIt's area is: {self.area()}\nIt's perimeter is: {self.perimeter()}"

class Rectangle:
    def __init__(self, a:float, b:float ):
        self.side_a = a
        self.side_b = b

    def perimeter(self)->float:
        return self.side_a*2+self.side_b*2

    def area(self)->float:
        return self.side_b*self.side_a

    def __str__(self):
        return f"Rectangle with sides of {self.side_a} and {self.side_b}.\nIt's area is: {self.area()}\nIt's perimeter is: {self.perimeter()}"

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f"Square with sides of {self.side}.\nIt's area is: {self.area()}\nIt's perimeter is: {self.perimeter()}"





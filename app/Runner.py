#!/usr/bin/env python3
from Shapes import Circle, Square, Rectangle


def main():

    TEXT = """
--------------------------------------------------------------------------
This application can calculate the area and parameter of squares, rectangles and circles.
Please select which shape's calculations you'd like to see:
[c] = circle
[s] = square
[r] = rectangle
[q] = quit 
--------------------------------------------------------------------------
    """
    options = ["c","s","r","q"]
    selection = input(TEXT)
    while selection not in options:
        selection = input("""
--------------------------------------------------------------------------
Try again! Your selection is not in the options provided!
[c] = circle
[s] = square
[r] = rectangle
[q] = quit 
--------------------------------------------------------------------------
""")
    match selection:
        case "c":
            c = input("Please enter the radius of the Circle! ")
            c = checker(c)
            print(Circle(float(c)))
        case "s":
            s = input("Please enter the size of the sides of the Square! ")
            s = checker(s)
            print(Square(float(s)))
        case "r":
            li = input("Please enter the size of the sides of the Rectangle! ").split()
            li[0] = checker(li[0])
            li[1] = checker(li[1])
            print(Rectangle(float(li[0]),float(li[1])))
        case "q":
            pass

def checker(to_be_checked):
    try:
        value = float(to_be_checked)
        if value <= 0:
            raise ValueError("Dimensions must be greater than zero.")
        return value
    except ValueError as e:
        return checker(input(f"""
--------------------------------------------------------------------------
{str(e).capitalize()}
I can only accept numbers when trying to calculate the area and the parameter
of a shape.
Please try again!
--------------------------------------------------------------------------
"""))


if __name__ == "__main__":
    main()
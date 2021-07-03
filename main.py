import math
import sys

# Circle Class


class Circle:
    def __init__(self, r: int) -> None:
        try:
            self.radius = r
            self.pi = math.pi
            self.result_area = self.pi * self.radius**2
            self.result_perimeter = 2 * self.pi * self.radius
        except ValueError:
            print("the program needs an integer")
            sys.exit()

    def area(self) -> str:
        """
        :arg self
        :return: self.result_area in a string
        """

        return f"the area of the circle is: {self.result_area}"

    def perimeter(self) -> str:
        """
        :arg self
        :return self.result_perimeter in a string
        """

        return f"the perimeter of the circle is: {self.result_perimeter}"

# Triangle Class


class Triangle:
    def __init__(self, h: int, b: int, right_side: int, left_side: int) -> None:
        try:
            self.height = h
            self.base = b
            self.right = right_side
            self.left = left_side
            self.result_area = b * h / 2
            self.result_perimeter = self.base + self.left + self.right
        except ValueError:
            print("the program needs an integer")
            sys.exit()

    def area(self) -> str:
        """
        :arg self
        :return self.result_area in a string.
        """

        return f"the area of a triangle is: {self.result_area}"

    def perimeter(self) -> str:
        """
        :arg self
        :return self.result_perimeter in a string.
        """

        return f"the perimeter of a triangle is: {self.result_perimeter}"


radius = input("enter the radius of the circle(int): ")

if radius.isdigit():
    radius = int(radius)
else:
    print("the program needs an integer")
    sys.exit()

circle = Circle(radius)

print(circle.area())
print(circle.perimeter())

height = input("enter the height of the triangle(int): ")
base = input("enter the base of the triangle(int): ")
right = input("enter the right side of the triangle(int): ")
left = input("enter the left side of the triangle(int): ")

triangle = Triangle(int(height), int(base), int(right), int(left))

print(triangle.area())
print(triangle.perimeter())

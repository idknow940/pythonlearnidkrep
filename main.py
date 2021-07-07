class Triangle:
    def __init__(self, base, left, right, height):
        try:
            self.base = float(base)
            self.left = float(left)
            self.right = float(right)
            self.height = float(height)
            self.area = (self.base * self.height) / 2
            self.perimeter = self.base + self.left + self.right

        except ValueError:
            raise ValueError('all sides of the class Triangle must be floats')

    def __new__(cls, *args, **kwargs):
        print(f"an instance of {cls}")
        return super(Triangle, cls).__new__(cls)

    def is_alike(self, other):
        if self.base == other.base and self.left == other.left and self.right == other.right:
            return True

    def __gt__(self, other):
        if self.base + self.left + self.right > other.base + other.left + other.right:
            return True
        else:
            return False

    def area(self):
        return self.area

    def perimeter(self):
        return self.perimeter

    def __del__(self):
        print(f"{self} was deleted.")

    def __str__(self):
        return f"an instance of Triangle"


class Cube:
    def __init__(self, side):
        try:
            self.side = float(side)
            self.volume = self.side ** 3
        except ValueError:
            raise ValueError('all sides of the class Cube must be floats')

    def volume(self):
        return self.volume

    def __gt__(self, other):
        if self.side > other.side:
            return True
        else:
            return False

    def area(self):
        return self.area

    def __new__(cls, *args, **kwargs):
        print(f"an instance of {cls}")
        return super(Cube, cls).__new__(cls)

    def __del__(self):
        print(f"{self} was deleted.")

    def __str__(self):
        return f"an instance of Cube"


class Rect:
    def __init__(self, side, side_2):
        try:
            self.side = float(side)
            self.side_2 = float(side_2)
            self.area = self.side * self.side_2
            self.perimeter = (self.side + self.side_2) * 2
        except ValueError:
            raise ValueError('all sides of the class Rect must be floats')

    def area(self):
        return self.area

    def perimeter(self):
        return self.perimeter

    def __gt__(self, other):
        if self.side * 2 + self.side_2 * 2 > other.side * 2 + other.side_2 * 2:
            return True
        else:
            return False

    def __new__(cls, *args, **kwargs):
        print(f"an instance of {cls}")
        return super(Rect, cls).__new__(cls)

    def __del__(self):
        print(f"{self} was deleted.")

    def __str__(self):
        return f"an instance of Rect"


tri_1 = Triangle(5, 10, 4, 5)
tri_2 = Triangle(5, 10, 4, 5)
cube_1 = Cube(5)
cube_2 = Cube(5)
rect_1 = Rect(5, 6)
rect_2 = Rect(5, 6)

print(tri_1, cube_1, rect_1, sep="\n")
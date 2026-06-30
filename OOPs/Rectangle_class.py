class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect1 = Rectangle(10, 5)
print(f"The area of the rectangle is {rect1.area()}")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

radius = float(input("Enter the radius of the circle: "))


circle1 = Circle(radius)
print(f"The area of the circle is {circle1.area()}")
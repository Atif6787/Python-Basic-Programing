class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("BMW", 19, 2026)
print(car1.brand, car1.model, car1.year)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Atif", 40000)
print(emp1.name, emp1.salary)
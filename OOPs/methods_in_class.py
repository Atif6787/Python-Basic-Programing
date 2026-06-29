class Student:
    
    # Default constructor
    def __init__(self):
        pass
    
    # Parameterized constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    # Method in Class
    def hello(self):
        print("Hello, my name is", self.name, "and my age is", self.age, "and my grade is", self.grade,".")


s1 = Student("Atif", 25, "A")
#print(s1.name, s1.age, s1.grade)
print(s1.hello())



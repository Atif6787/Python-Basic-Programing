class Student:

    # Default constructor
    def __init__(self):
        pass
    
    # Parameterized constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        print("Adding a new students in Database...")


s1 = Student("Atif", 25, "A")
print(s1.name, s1.age, s1.grade)

s2 = Student("Ali", 22, "B")
print(s2.name, s2.age, s2.grade)

s3 = Student("Ahmed", 23, "C")
print(s3.name, s3.age, s3.grade)


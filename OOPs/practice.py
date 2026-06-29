
# Let's Practice Methods in Class
'''Create student class that takes name and marks of 3 subgjects as arguments i constructor. 
Then create a method to print the average marks of the student.'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Average marks of", self.name, "is", sum / 3)

s1 = Student("Atif", [80, 90, 70])
s1.average()
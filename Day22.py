class Student:

    college = "ABC College"       # Class variable

    def __init__(self, name, marks):
        self.name = name           # Instance variable
        self.marks = marks         # Instance variable

    def display(self):
        message = "Student Details"    # Local variable

        print(message)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("College:", Student.college)


s1 = Student("Sajid", 85)
s2 = Student("Harshini", 74)

s1.display()

print()

s2.display()
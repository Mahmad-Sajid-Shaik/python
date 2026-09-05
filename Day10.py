#Dictionary Program:
student = {
    "name": "Sajid",
    "age": 21,
    "course": "Python",
    "marks": 85
}

print("Original Dictionary:", student)

print("\nDictionary Operations")

print("Access:", student["name"])
print("Membership:", "name" in student)
print("Not Membership:", "city" not in student)

student["city"] = "Hyderabad"
print("After Adding:", student)

student["marks"] = 90
print("After Updating:", student)

print("\nDictionary Functions")

print("Length:", len(student))
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

print("\nDictionary Methods")

print("Get Name:", student.get("name"))
print("Get City:", student.get("city"))

student.setdefault("phone", "9999999999")
print("Setdefault:", student)

student.update({"marks": 95, "college": "ABC College"})
print("Update:", student)

copy_student = student.copy()
print("Copy:", copy_student)

student.pop("phone")
print("Pop:", student)

student.popitem()
print("Popitem:", student)

# if and if-else Statement Program:

name = input("Enter student name: ")
age = int(input("Enter age: "))

maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
english = int(input("Enter English marks: "))

total = maths + python + english
percentage = total / 3

print("\n----- STUDENT DETAILS -----")
print("Name:", name)
print("Age:", age)
print("Total:", total)
print("Percentage:", percentage)

if age >= 18:
    print("Age: Eligible")
else:
    print("Age: Not Eligible")

if maths >= 40 and python >= 40 and english >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

if percentage >= 90:
    print("Grade: A+")
else:
    if percentage >= 80:
        print("Grade: A")
    else:
        if percentage >= 70:
            print("Grade: B")
        else:
            if percentage >= 60:
                print("Grade: C")
            else:
                print("Grade: D")

if percentage >= 90:
    print("Scholarship: Eligible")
else:
    print("Scholarship: Not Eligible")

if age >= 18:
    if percentage >= 60:
        print("Admission: Approved")
    else:
        print("Admission: Not Approved")
else:
    print("Admission: Not Approved")
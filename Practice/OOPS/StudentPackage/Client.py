from Student import Student

Student1 = Student("John", 20, 101)
print(Student1.name)
print(Student1.age)
print(Student1.roll_no)
print(Student1.displayStudent())

Student2 = Student("Alice", 22, 102)
print(Student2.name)
print(Student2.age)
print(Student2.roll_no)
print(Student2.displayStudent())

# We are creating two instances of the Student class, Student1 and Student2.
# Each instance has its own attributes: name, age, and roll_no.
# The code then prints the attributes of each student instance.
# This demonstrates how to create and use objects in Python using a class.
# The output will show the name, age, and roll number of each student.
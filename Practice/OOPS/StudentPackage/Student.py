class Student:
    def __init__(self, name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
    
    def displayStudent(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}") # -- This object level method
    

# The __init__ method is a special method in Python classes that initializes the object's attributes.
# It is called when an object of the class is created.
# In this case, it initializes the attributes name, age, and roll_no for each Student object.
# The self parameter refers to the instance of the class itself, allowing access to its attributes and methods.

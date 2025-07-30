number = (1,2,3,4)
# This code demonstrates how to create a tuple in Python.

print(number)
# Tuples are immutable, meaning their elements cannot be changed after creation.
print(number[0])
# This code demonstrates how to access the first element of a tuple in Python.

print(number[1])
# This code demonstrates how to access the second element of a tuple in Python.

number[0] = 5
# This line will raise a TypeError because tuples are immutable and cannot be modified.
print(number)

# Once a tuple is created, you cannot change its elements.
# To create a new tuple with modified elements, you would need to create a new tuple entirely.




name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello "+name+" !" + " You are "+ age + " years old.")

# This code demonstrates how to take user input for a name and age, and then print a greeting message.
# It uses the `input` function to get input from the user and concatenates the strings to form a complete message.
# Note: The above code does not handle type conversion for age, so it will be treated as a string.
# To convert the age to an integer, you can use:
# age = int(input("Enter your age: "))
# This will allow you to perform numerical operations on the age if needed.
# However, for the purpose of this example, we are keeping it as a string for simplicity.
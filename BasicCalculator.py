num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = float(num1) + float(num2)
print("The sum is: " + str(result))


# This code demonstrates how to take two numbers as input from the user, convert them to floating-point numbers,
# and then calculate and print their sum. It uses the `input` function to get input from the user,
# converts the inputs to `float` for numerical operations, and finally prints the result as a string.
# Note: The above code assumes that the user will enter valid numeric inputs.
# If the user enters non-numeric values, it will raise a ValueError.
# If we want to restrict user to only enter whole numbers which is an integer, we can use:
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = num1 + num2
# Or we can do result =  int(num1) + int(num2)
# This will ensure that the inputs are treated as integers for addition.

import BasicCalculator as calc

num1 = int(input("Enter the num1 : "))
num2 = int(input("Enter the num2 : "))
operator = input("Enter the operator (+, -, *, /): ")
result = calc.calculator(num1, num2, operator)

print("Result:", result)

# This code imports the BasicCalculator module and uses its calculator function to perform a calculation based on user input.
# It prompts the user to enter two numbers and an operator, then calls the calculator function with these inputs.




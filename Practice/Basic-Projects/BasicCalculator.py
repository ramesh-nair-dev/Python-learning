def calculator(num1 , num2 , operator):
    if(operator == '+'):
        return num1 + num2
    elif(operator == '-'):
        return num1 - num2
    elif(operator == '*'):
        return num1 * num2
    elif(operator == '/'):
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator. Please use +, -, *, or /."
    

# print(calculator(5, 10, '+'))  # Example usage
# print(calculator(10, 5, '-'))  # Example usage 
# print(calculator(5, 10, '*'))  # Example usage
# print(calculator(10, 5, '/'))  # Example usage
# print(calculator(10, 0, '/'))  # Example usage with division by zero
# print(calculator(10, 5, '%'))  # Example usage with invalid operator


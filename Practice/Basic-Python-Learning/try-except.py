try:
    value = 10/0
    num = int(input("Enter the number"))
    print(num)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# This code attempts to perform a division by zero, which will raise a ZeroDivisionError.
# It also includes a prompt for user input to enter an integer.
# If the input is not a valid integer, it will raise a ValueError.
# The code uses try-except blocks to handle these exceptions gracefully.
# If a ValueError occurs, it prints a message asking for a valid integer.
# If a ZeroDivisionError occurs, it prints a message indicating that division by zero is not allowed.
# The code demonstrates basic exception handling in Python, allowing the program to continue running without crashing when an error occurs.
# This is useful for ensuring that the program can handle unexpected input or errors without terminating abruptly.
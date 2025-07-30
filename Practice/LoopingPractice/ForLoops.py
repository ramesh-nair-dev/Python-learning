rows = int(input("Enter the number of rows: "))
for i in range(rows+1):
    print("*" * i)

# This code prompts the user to enter the number of rows and then uses a for loop to print a right-angled triangle pattern of asterisks.
# The loop iterates from 0 to the number of rows specified by the user.
# In each iteration, it prints a line with a number of asterisks equal to the current iteration index `i`.
# The first iteration prints 0 asterisks, the second prints 1 asterisk, and so on, up to the specified number of rows.
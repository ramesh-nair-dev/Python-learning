def max(num1 , num2 , num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 > num1 and num2 >= num3:
        return num2
    else:
        return num3
    

print(max(3, 7, 5))

# When we can say the num1 is max num among three number when num1 is greater than or equal to num2 and num3.
# When num2 is greater than num1 and greater than or equal to num3 then num2 is max num.
# When both above conditions are false then num3 is max num.
# This code defines a function called max that takes three numbers as input and returns the maximum of the three.
# The function uses if-elif-else statements to compare the numbers and determine which one is the largest.
# The function is then called with three numbers, and the result is printed to the console.

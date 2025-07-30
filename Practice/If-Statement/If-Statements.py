is_male = False
is_tall = True

if is_male:
    print("You are a male") # ---- All code that needs to executed in the if statement must be indented
else:
    print("You are not a male")
print("This is outside the if statement") # ---- This code will always be executed regardless of the if statement


if is_male and is_tall:
    print("You are tall male") # ---- This code will only be executed if both conditions are true
elif is_male and not(is_tall):
    print("You are short male") # ---- This code will be executed when is_male is true and is_tall is false what happens here is that # the not operator negates the value of is_tall, so if is_tall is false, not(is_tall) will be true
elif not(is_male) and is_tall:
    print("You are tall but not male") # ---- Will execute when is_male is false and is_tall is true
else:
    print("You are neither male and tall") # ---- This will execute when all above conditions are false

# ---- This code demonstrates how to use if statements in Python.
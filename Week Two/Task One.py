
# Task 1: Basic calculations

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculations
print("Sum:", num1 + num2)
print("Product:", num1 * num2)
print("First minus second:", num1 - num2)

# Division needs a non-zero second number
if num2 != 0:
    print("Division:", num1 / num2)
    print("Integer division:", num1 // num2)
    print("Modulus:", num1 % num2)
else:
    print("Cannot divide by zero.")

# Raise the first number to the power of the second
print("Power:", num1 ** num2)
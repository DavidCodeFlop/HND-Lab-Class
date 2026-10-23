
# Task 4: Odd or even

number = int(input("Enter a positive integer (1-100): "))

if number < 1 or number > 100:
    print("Error: Number must be between 1 and 100.")

elif number % 2 == 0:
    print(number, "is even.")

else:
    print(number, "is odd.")

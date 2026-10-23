
# Task 5: Multiplication table

number = int(input("Enter a number: "))

for i in range(1, 11):
    answer = number * i
    print(number, "x", i, "=", answer)

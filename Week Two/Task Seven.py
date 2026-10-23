
# Task 7: Fibonacci sequence

first = 0
second = 1

for i in range(20):
    print(first, end=" ")

    # Calculate the next term
    next_term = first + second

    # Move the values forward
    first = second
    second = next_term

print()  # Move to a new line


# Task 3: Egg converter

eggs = int(input("Enter the number of eggs: "))

# Find the number of gross
gross = eggs // 144

# Find the eggs left after removing gross
remaining = eggs % 144

# Find the number of dozens
dozens = remaining // 12

# Find the single eggs left
singles = remaining % 12

print(
    eggs, "eggs is",
    gross, "gross eggs +",
    dozens, "dozen eggs +",
    singles, "eggs"
)
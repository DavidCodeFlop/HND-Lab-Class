
# Task 6: Password checker

correct_password = "python123"

password = input("Enter the password: ")

while password != correct_password:
    print("Incorrect password. Try again.")
    password = input("Enter the password: ")

print("Access granted!")

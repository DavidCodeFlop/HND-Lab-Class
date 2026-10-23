password = input("Enter your password: ")
 
uppercase = 0
lowercase = 0
numbers = 0
symbols = 0
 
for char in password:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        numbers += 1
    else:
        symbols += 1
 
print("Password Length:", len(password))
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Numbers:", numbers)
print("Symbols:", symbols)

if __name__ == "__main__":
    main()
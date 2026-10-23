allowed_symbols = "!@#$%"
 
while True:
    password = input("Enter your password: ")
 
    uppercase = 0
    lowercase = 0
    numbers = 0
 
    for char in password:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            numbers += 1
 
    has_symbol = False
 
    for char in password:
        if char in allowed_symbols:
            has_symbol = True
 
    no_spaces = " " not in password
 
    if (len(password) >= 10
            and uppercase >= 1
            and lowercase >= 1
            and numbers >= 2
            and has_symbol
            and no_spaces):
        print("Password accepted!")
        break
    else:
        print("Invalid password. Please try again.")


if __name__ == "__main__":
    main()
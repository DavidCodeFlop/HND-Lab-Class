def validate_password(password):
    if len(password) < 10:
        return False
 
    if not any(char.isupper() for char in password):
        return False
 
    if not any(char.islower() for char in password):
        return False
 
    if sum(char.isdigit() for char in password) < 2:
        return False
 
    if not any(char in "!@#$%" for char in password):
        return False
 
    if " " in password:
        return False
 
    return True
 
 
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
 
    if validate_password(password):
        print("Password accepted! Account can be created.")
        break
    else:
        print("Invalid password. Please try again.")

if __name__ == "__main__":
    main()
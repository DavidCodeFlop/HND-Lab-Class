def authenticate(username, password):
    if username == "admin" and password == "admin123":
        return True
    else:
        return False
 
 
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
 
    if authenticate(username, password):
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Try again.")

if __name__ == "__main__":
    main()
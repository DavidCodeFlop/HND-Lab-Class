
# TASK 8: BASIC CYBERSECURITY TOOL

# Demo credentials for this lab exercise
startup_password = "start123"
correct_password = "secure123"
correct_username = "admin"


print("Welcome to the Security Tool")

password = input("Enter the startup password: ")

while password != startup_password:
    print("Incorrect password.")
    password = input("Enter the startup password: ")

print("Authentication successful!")



while True:

    print("\n===== SECURITY MENU =====")
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")


    if choice == "1":

        correct_count = 0
        incorrect_count = 0

        for i in range(10):
            entered_password = input("Enter password: ")

            if entered_password == correct_password:
                correct_count += 1
            else:
                incorrect_count += 1

        incorrect_percentage = (incorrect_count / 10) * 100

        print("Correct passwords:", correct_count)
        print("Incorrect passwords:", incorrect_count)
        print("Incorrect percentage:", incorrect_percentage, "%")

        if incorrect_percentage > 50:
            print("ALERT: More than 50% of passwords were incorrect!")
        else:
            print("No alert required.")


 

    elif choice == "2":

        brute_password = "cyber123"
        max_attempts = 5
        attempts = 0
        success = False

        while attempts < max_attempts:

            guess = input("Guess the password: ")
            attempts += 1

            if guess == brute_password:
                print("Correct password!")
                success = True
                break
            else:
                print("Incorrect guess.")

        print("Attempts used:", attempts)

        if success:
            print("Simulation successful.")
        else:
            print("Maximum attempts reached.")




    elif choice == "3":

        failed_logins = 0
        authenticated = False

        while failed_logins < 3:

            username = input("Enter username: ")
            password = input("Enter password: ")

            if (username == correct_username
                    and password == correct_password):

                print("Login successful!")
                authenticated = True
                break

            else:
                failed_logins += 1
                print("Login failed.")

                remaining = 3 - failed_logins

                if remaining > 0:
                    print("Attempts remaining:", remaining)

        if not authenticated:
            print("Account frozen for 24 hours.")


    elif choice == "4":
        print("Thank you for using the security tool")
        break

    else:
        print("Invalid option. Please select 1, 2, 3 or 4.")

import random
from datetime import datetime
import socket
 
# Correct login details for this exercise
correct_username = "admin"
correct_password = "SecurePass123!"
 
# Find the local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
try:
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
except OSError:
    ip_address = "127.0.0.1"
finally:
    s.close()
 
print("SECURITY EVENT LOG")
 
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
 
    # Generate an event ID and timestamp for this attempt
    event_id = random.randint(1000, 9999)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
    # Check the login details
    if (username == correct_username
            and password == correct_password):
        event = "Successful login"
    else:
        event = "Failed login"
 
    # Print the event log
    print("\nEvent ID:", event_id)
    print("Username:", username)
    print("IP Address:", ip_address)
    print("Event:", event)
    print("Timestamp:", timestamp)
 
    if event == "Successful login":
        print("Login successful!")
        break
    else:
        print("Incorrect username or password. Try again.")

if __name__ == "__main__":
    main()
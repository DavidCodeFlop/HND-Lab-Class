# Introduce file to user.
print("This is a security form. Please input all of the required information in the boxes below.")

# Get info from user.
name = input("Please enter your name: ")
Banner_ID = input("Please enter your Banner ID: ")
IP_Address = input("Please enter the IP Address: ")
Security_Events = input("Please enter the number of security events: ")

# Display all given infromation
print("Below is all given information")

print("Your Name is ", name)
print("Your Banner ID is ", Banner_ID)
print("Your IP Address is ", IP_Address)
print("Your number of Security Events listed is ", Security_Events)

print("Thank you for giving us all of this information. We will not get back to you anytime soon. Goodbye.")
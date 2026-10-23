event = (
    "Security Alert: Failed login attempt detected from IP "
    "address 192.168.1.25. The user account admin was targeted "
    "at 22:45. The server blocked the login attempt after an "
    "incorrect password was entered."
)
 
print("Security Event Analysis")
 
# Check for the word Failed
if "Failed" in event:
    print("Failed event: Yes")
    print("Warning: A failed security event was detected.")
else:
    print("Failed event: No")
 
# Check for the word login
if "login" in event.lower():
    print("Login event: Yes")
    print("Login activity detected.")
else:
    print("Login event: No")
 
# Extract the IP address
ip_address = ""
 
for word in event.split():
    if word.startswith("192.168."):
        ip_address = word.rstrip(".")
        break
 
print("IP Address:", ip_address)
 
if "Failed" in event and "login" in event.lower():
    print("Action: Investigate the failed login attempt.")

if __name__ == "__main__":
    main()
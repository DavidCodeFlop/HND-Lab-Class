def validate_ip(ip):
    ip = ip.strip()
 
    if "." not in ip:
        return False
 
    if ip.count(".") != 3:
        return False
 
    parts = ip.split(".")
 
    if len(parts) != 4:
        return False
 
    for part in parts:
        if not part.isdigit():
            return False
 
        number = int(part)
 
        if number < 0 or number > 255:
            return False
 
    return True
 
 
ip_address = input("Enter an IP address: ")
 
if validate_ip(ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")

if __name__ == "__main__":
    main()
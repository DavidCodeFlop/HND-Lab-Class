def calculate_failed_percentage(failed, total):
    return (failed / total) * 100
 
 
try:
    failed = int(input("Enter number of failed login attempts: "))
    total = int(input("Enter total login attempts: "))
 
    percentage = calculate_failed_percentage(failed, total)
 
    print(f"Failed login percentage: {percentage:.2f}%")
 
    if percentage >= 50:
        print("HIGH RISK")
    elif percentage >= 25:
        print("MEDIUM RISK")
    else:
        print("LOW RISK")
 
except ValueError:
    print("Please enter numbers only.")
 
except ZeroDivisionError:
    print("Total login attempts cannot be zero.")
 
except TypeError:
    print("Invalid input type. Please enter valid numbers.")
 
except Exception:
    print("An unexpected calculation error occurred.")

if __name__ == "__main__":
    main()
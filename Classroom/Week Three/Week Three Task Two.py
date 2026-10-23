logins = [2, 7, 1, 12, 4, 9]
failed_logins = [login for login in logins if login > 5]
print("These are all of the failed login attempts:", failed_logins)
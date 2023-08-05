password = input("Enter a password: ")

if len(password) > 7:
    print("Great password there!")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak")
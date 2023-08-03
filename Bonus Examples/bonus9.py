# Application That checks the strength of a password

password = input("Enter new Password: ")
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")



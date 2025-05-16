# correct email - campusx@hgmail.com
# password - 1234

email = input("Enter your email:")

if '@' in email:
    password = input("Enter your password:")
    if email == "campusx@gmail.com" and password == "1234":
        print("Login successful")
    elif email == "campusx@gmail.com" and password != "1234":
        print("Incorrect password")
        password = input("Enter your password again:")
        if password == "1234":
            print("Finally correct password, Welcome to campusx")
        else:
            print("incorrect password")
else:
    print("Enter a valid email")
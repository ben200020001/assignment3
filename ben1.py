correctusername = "admin"
correctpassword = "bernard"

for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correctusername and password == correctpassword:
        print("login successful")
        break
    else:
        print("incorrect username or password")
    if i == 2:
        print("login failed.Please try again later")

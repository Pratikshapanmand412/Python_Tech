#WAP to check if user has entered correct userid and password
user_id = input("Enter userid:")
password = int(input("Enter password: "))

if(user_id== "vaishu") and (password == 12345):
    print("You can login")
else:
    print("Invalid input")
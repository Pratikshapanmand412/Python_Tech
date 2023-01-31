#WAP to prompt user to enter userid and password .If id and password is incorrect
#give him chance to re-enter the credentials.Let him try 3 times.After that program to terminate.
user_id = input("Enter userid: ")
password = int(input("Enter password: "))

if(user_id == "pratiksha") and (password == 98765):
    print("Login successful....")
else:
    print("Re-enter credentials...")
    for i in range(1,4):
        user_id = input("Enter userid:")
        password = int(input("Enter password: "))
        if(user_id == "pratiksha") and (password == 98765):
            break
           
    print("Login successful...")
            
   
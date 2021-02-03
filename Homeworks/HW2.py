#GlobalAIHub Homework 2

#user name and password specified
#UserName and Password
user_name="vonuryil"
password="globalaihub46@"
#get from user
get_user_name=input("User Name: ")
get_password=input("password: ")
#check if it is true
if (user_name == get_user_name and password==get_password):
    print("Access Granted")
else:
    print("Access Denied")
    
user_info={"user_name":"vonuryil","password":"dumbpassword"}
get_d_username=input("Dictionary Username: ")
get_d_password=input("Dictionary Password: ")
if (user_info["user_name"] == get_d_username and user_info["password"]==get_d_password):
    print("Access Granted")
else:
    print("Access Denied")




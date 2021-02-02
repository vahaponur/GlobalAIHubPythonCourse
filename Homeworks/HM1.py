#GlobalAIHub Introduction to Python Homework1
# A list maded 0,13
homeworklist=list(range(14))
#list's second half swapped with first half
homeworklist.reverse()
#In homework, there was no exp what kind of print so I print one by one
i=0
for item in homeworklist:
     print(homeworklist[i])
     i+=1
#question 2

n=int(input("Please enter an integer between 0-10: "))
#check if it is between 0-10
while n<0 or n>10:
    print("You entered an invalid value")
    #if it's not ask again until it is
    n=int(input("Please enter an integer between 0-10: "))
modlist=list(range(n+1))
odd_squares = [i for i in modlist if i% 2 == 1]
print("Odd numbers 0 to your value are:",odd_squares)
request=input("If you want to continue type 'move', to finish type 'finish' : ")
while request != "finish" and request != "move":
    request=input("Wrong!!! to continue type 'move', to finish type 'finish': ")
    
while request == "move":
 n=int(input("Please enter an integer between 0-10: "))
 #check if it is between 0-10
 while n<0 or n>10:
    print("You entered an invalid value")
    #if it's not ask again until it is
    n=int(input("Please enter an integer between 0-10: "))
 modlist=list(range(n+1))
 odd_squares = [i for i in modlist if i% 2 == 1]
 print("Odd numbers 0 to your value are:",odd_squares)
 request=input("If you want to continue type 'move', to finish type 'finish': ")
 while request != "finish" and request != "move":
     request=input("Wrong!!! to continue type 'move', to finish type 'finish': ")
 if request=="finish":
     break
#Global AI Hub Homework 3 day 4
#defining function
def f():
    
    list1=list(range(0,100))
    for item in list1:
#checking if it is gretaer than 1
       #if not >1 go back to the loop and get another 
        if item<=1:
         continue 
     
     #divide the number with all the smaller number from it to check it is not prime
        for i in range(2,item):
            if item%i==0:
             break
         
        else:
            print(item)
f()
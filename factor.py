a=int(input("enter the number"))
c=a%3
b=a%7
if(c==0 and b!=0):
   print("number is devisible by 3")
elif(c==0 and b==0):
    print("number is devisible by 3 or 7")
elif(c!=0 and b==0):
    print("number is devisible by 7")
elif(c!=0 and b!=7):
    print("number is not devisible")


    


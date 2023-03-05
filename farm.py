H=int(input("enter the no of head->"))
L=int(input("enter the no of legs->"))
b=L/53
cl=b*15/2
gl=b*38/4
a=H/34
CH=15*a
GH=19*a
if(cl==CH and gl==GH):
   print("no of chicken->",CH)
   print("no of goat->",GH)
else:
    print("invalid values")
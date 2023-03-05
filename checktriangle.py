print("input lengths of the triangle side")
X=int(input("X:"))
Y=int(input("Y:"))
Z=int(input("Z:"))
if X==Y==Z:
    print("equilateral trinagle")
elif X**2+Y**2==Z**2:
    print("right angled triangle")
elif X==Y or Y==Z or Z==X:
    print("issosceles triangle")
else:
    print("Scalene triangle")        

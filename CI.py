P=int(input("enter the principle value->"))
R=int(input("enter the rate->"))
T=int(input("enter the time->"))
A=P*((1+R/100)**T)
CI=A-P
print("compound interest:",CI)

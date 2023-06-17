import math
p=float(input("Enter the principal="))
r=float(input("Enter the rate of interst="))
n=float(input("Enter the tenure="))
c=(p*r*(math.pow((1+r),n)))/(math.pow((1+r),n-1))
print("The emi is",c)




import math
a=float(input("Enter the first side of triangle"))
b=float(input("Enter the second side of triangle"))
c=float(input("Enter the third side of triangle"))
s=(a+b+c)/2
d=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of triangle by herons formula =",d)











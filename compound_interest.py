p=float(input("Enter the principal"))
r=float(input("Enter the rate of interest"))
t=float(input("Enter the time"))
n=float(input("Enter the number of interest compounded per year"))
a=p*((1+(r/n))**(n*t))
print("the compound interst is",a)


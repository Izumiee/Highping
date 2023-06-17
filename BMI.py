
import math
a=float(input("Enter weight of student in kg"))
b=float(input("Enter height of student in cm"))
c=(a/(math.pow(b,2)))
if(c<18.5):
    print("Underweight")
elif(c>=18.5 and c<14.9):
    print("Normal")
elif(c>=25.0 and c<=29.9):
    print("Overweight")
else:
    print("Obese")
    




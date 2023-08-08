import math
a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
if (math.pow(b,2)-4*a*c)>=0:
    k=(-b+(math.sqrt(math.pow(b,2)-4*a*c)))/(2*a)
    kk=(-b-(math.sqrt(math.pow(b,2)-4*a*c)))/(2*a)
    print("Roots are: ",kk,k)

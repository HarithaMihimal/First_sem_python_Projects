#Conditional Control Structures

a=int(input("Enter angle 1: "))
b=int(input("Enter angle 2: "))
c=int(input("Enter angle 3: "))
angle=90
if (a+b+c)==180 and a>0 and b>0 and c>0:
    if a==angle or b==angle or c==angle:
        print("Right angled")
    elif a<angle and b<angle and c<angle:
        print("Acute angled")
    else:
        print("Obtuse angled")

else:
    print("Angles do not form a triangle")

enter=input()
enter1=enter.split()
y=int(enter1[0])
m=int(enter1[1])
d=int(enter1[2])
if m<3:
    m=m+12
    y=y-1
a=2*m+6*(m+1)//10
b=y+y//4-y//100+y//400
f1=d+a+b+1
f=f1%7
print(f)

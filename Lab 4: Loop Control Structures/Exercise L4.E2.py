num=int(input("Input number: "))
if num>=2:
    totel2=0
    for i in range(2,num+1):
        totel1=0
        for j in range(1,i):
            if i%j==0:
                totel1+=j
        if totel1>i:
            totel2+=1

    print("Number of abundant numbers from 1 to %d is %d"%(num,totel2))

else:
    print("Invalid Input")

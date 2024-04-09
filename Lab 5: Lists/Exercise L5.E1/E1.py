Input=input().split() #10  separated numbers
if len(Input)==10:
    lst=[]                      #define a empty list
    for i in Input:
        value1=float(i)         #convert string i to float value
        value2=str(value1)      #convert float  to string value
        if value2==i:           #chack converted values are integers or floats
            lst.append(value1)  #remake list
        else:
            lst.append(int(i))  #remake list

    print("Minimum =",min(lst)) #print maximum and minimum values of the new list
    print("Maximum =",max(lst))

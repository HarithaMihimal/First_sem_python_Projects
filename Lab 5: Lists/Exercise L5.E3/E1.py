lst1=[] #define empty list
for i in range(4): #get four inputs repeatly 4 times
    lst2=[]  #define anyother list
    Input_Marks=input().split() #get input and create space separate list
    if len(Input_Marks)==3:   #check number of subjects is equas to 3 
        for j in Input_Marks:
            lst2.append(int(j))  #string list convert to integer list 
        lst1.append(lst2)
for i in lst1:
    total=sum(i) #get summetion in small list
    length=len(i)#get length of small list
    average=total/length  #get avarege value
    print("Total: %s Average: %.1f"%(total,average))

st=input("Enter message: ")
num=int(input("Enter base: "))
k=""
if num>1 and num<=10:
    for i in st:
        kk=""
        aski=ord(i)
        l=0
        while l==0:
            p=aski%num
            kk=str(p)+kk
            if aski//num==0:
                l=1
            aski=aski//num
        k=k+kk
    print(k)

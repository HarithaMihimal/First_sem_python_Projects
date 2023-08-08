wFlag=True                  #while loop flag
while wFlag:
    fFlag=True              #factor falg
    num=int(input())        #input Integer
    if num==0 or num==1:    #0,1 are not primes
        fFlag=False
    elif num<=-1:           #terminate condition
        #wFlag = False
        break

    elif num>1:             #for positive integers
        for i in range(2,num):
            if num%i==0:
                fFlag=False
                break

    if fFlag:           
        print("prime")
    else:
        print("non-prime")

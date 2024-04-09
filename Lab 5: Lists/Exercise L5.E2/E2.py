Input=input().split()           #names of two sports
if len(Input)==2:               #conferm input is the two sports

    lst1=["I","We"]
    lst2=["play","watch"]

    for i in lst1:              #nested loop
        for j in lst2:
            for k in Input:
                print(i,j,k+".")#output

try:
    matrix1=[]
    while True:
        Input=input()
        if Input=="-1":
            break
        else:
            lst1=[]
            lst2=Input.split()
            for i in lst2:
                lst1.append(int(i))
            matrix1.append(lst1)
    lenth=len(matrix1[0]) #number of columns

    for i in matrix1:    #chack validity of the matrix
        if lenth!=len(i):
            print("Invalid Matrix")
            break
    else:
        lenth2=len(matrix1) #number of rows
        result=[[0 for i in range(lenth2)]for j in range(lenth)]


        for i in range(lenth):
            for j in range(lenth2):
                result[i][j]=matrix1[j][i]  #change position elements

        for i in range(lenth):
            for j in range(lenth2):
                print(format(str(result[i][j]),"<2"),end="") #print matrix elements in two space distence
            print()

except ValueError:
    print("Error")

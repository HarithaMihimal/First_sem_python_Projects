try:

    def CREAT_MATRIX():  # Entering elements for the matrix

        global matrix    # declaration of global variable for matrix
        matrix = [list(map(int, input().split())) for i in range(row)]  # geting  space separate user inputs for matrix
        return matrix  # return matrix


    def TRANSPOSE_MATRIX(matrix_Transe_B): # transpose metrix of matrix B
        for i in range(col):
            lst = []  # ctreating extra list for creating 2D list
            for j in range(row):
                lst.append(matrix_B[j][i])
            matrix_Transe_B.append(lst)
        return matrix_Transe_B  # return transpose matrix B


    def MULTIPLICATION_MATRIX(matrix_OUT):

        for i in range(row):
            lst = []  # ctreating extra list for creating 2D list
            for k in range(row): 
                total = 0
                for j in range(col):
                    total += matrix_A[i][j] * matrix_Transe_B[j][k]  # taking sum of the multipings
                    if j == len(matrix_A[0]) - 1:
                        lst.append(total)  # modifying list by appending sums
            matrix_OUT.append(lst)
        return  matrix_OUT # return matrix A X Transpose matrix B


    def PRINT_MATRIX():  # output values of matrix A X (transpose marix B) in row wise
        for i in range(row): #looping through rows
            for j in range(row): #looping through columns
                print(matrix_OUT[i][j], end=" ") 
            print()
        return


    dimension = input("Enter the dimension: ")  # input dimentions of matrices
    dimension_list = list(map(int, dimension.split(","))) #input string convert to the int list

    row = dimension_list[0] #number of rows
    col = dimension_list[1] #number of columns
    print("Enter Matrix A:")
    matrix_A = CREAT_MATRIX()  # call the function

    flag1 = 0  # cheking whether number of elements in a row is equal to the number of columns in the matrix A
    for i in matrix_A:
        if len(i) != col:
            flag1 = 1

    if flag1 == 0:
        print("Enter Matrix B:")
        matrix_B = CREAT_MATRIX()

        for i in matrix_B:  # cheking whether number of elements in a row is equal to the number of columns in the matrix B
            if len(i) != len(matrix_B[0]):
                flag1 = 1

        if flag1 == 0:      # considering the accuracy of the matrices
            matrix_Transe_B = []
            TRANSPOSE_MATRIX(matrix_Transe_B)  # calling the TRANSPOSE_MATRIX() function for get transpose of the matrix B
            matrix_OUT = []
            MULTIPLICATION_MATRIX(matrix_OUT)  # calling the MULTIPLICATION_MATRIX() function for get multiplication of matrices
            PRINT_MATRIX()  # calling the PRINT_MATRIX() function for print output matrix


        else:
            print("Invalid Matrix")


    else:
        print("Invalid Matrix")
except:  # handling exceptions
    print("Error")

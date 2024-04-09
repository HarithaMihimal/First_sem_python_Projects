try: # checking incompatible values and any other errors

    file_name = input()     # getting user input for name of input file

    def getNum(file_name):  # function to read the number n from the file
        text = open(file_name, "r")  # opening the given file
        n = text.read()     # reading the value of n
        text.close()        # close the opened file
        n=int(n)            # converting string value to integer
        return n



    def Fibonacci(n): #function to creating the Fibonacci sequence value
        pre_value=0   # store first elemant
        after_value=1 # store second elemant
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(2, n + 1): 
                c_ =after_value+pre_value #obtaining sum of nearest values
                pre_value = after_value
                after_value = c_
            return after_value  #return result value

    def show(n):    # function to display the given value n and the computed value of Fibonacci value
        y = Fibonacci(n) # calling the Fibonacci function
        y = "Fibonacci(" + str(n) + ") = " + str(y)     # creating correct output format
        print(y)    # display the created output
        return y

    def saveFile(y):# function to write what was displayed in return show function 
        a = open("result.txt", "w") # opening new text file 
        a.write(y)  # writing string on created file
        a.close()   # closing opened file

except:     # run if  errors generated
    print("Invalid input.")
else:       # run if no errors generated
    value_n=getNum(file_name)   # calling function to get the value in the file
    if 0 <= value_n <= 20:      # check given conditions
        
        output=show(value_n)    # calling function to get the string in the "show" function
        #print(output)
        saveFile(output)        # calling function to write the returned phrase
    else:
        print("Invalid input.")

from datetime import datetime
from cs1033_evaluator import evaluate_lab7


def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################
file_name=input()  #getting file name as user input
file1=open(file_name,"r")   
file2=open("output.txt","w")  #creating a new file to write the new txt
READ=file1.read()
READ_LIST=READ.split("\n")  # informations of the file convert to list
lst2=[]
if READ_LIST[-1]=="": #checking empty string in the last element of the list
    READ_LIST.pop()   #remove the empty string
else:
    READ_LIST=READ_LIST
for i in READ_LIST:  #Iterate READ_LIST for creating birth years list
    date=i.split()[1]
    
    datetime_object = datetime.strptime(date, "%Y-%m-%d") # Convert the date string to a datetime object

    date=datetime_object.year # Extract only the year and remove the timestamp
    
    lst2.append(str(date))

lst4=list(set(lst2)) # remove same eliments from lst2 by using set function
for i in lst4: #Iterating loop for get the count and numbering elements
    total=0
    for j in range(len(READ_LIST)):
        if i==READ_LIST[j].split()[1][0:4]:
            total+=1 #getting count
            READ_LIST[j]=READ_LIST[j]+" "+str(total) #update the READ_LIST with count


for i in READ_LIST:# Iterating new updated list
    #print(i)
    B = i.split() #separatting elemants of the list
    date = B[1] #store birthday 
   
    total = days_to_birthday(date) #call the days_to_birthday function 
    if B[-2] == "F": #check male or female 
        total += 500 #adding  500 to that value
        total = str(total)
    elif B[-2] == "M":  #check male or female 
        total = str(total)
        if len(total) == 1: #check length of string
            total = "00" + total #create new string  by adding 0s till length=3
        elif len(total) == 2: #check length of string
            total = "0" + total #create new string  by adding 0s till length=3

    if len(B[-1]) == 1: #check length of string B[-1]
        B[-1] = "00" + B[-1] #remake string B[-1] by adding 0s prifix of the string
    elif len(B[-1]) == 2:
        B[-1] = "0" + B[-1] #remake string B[-1] by adding 0s prifix of the string

   

    newSTRING = B[0] + " " + date[0:4] + total+B[-1]
   
    file2.write(newSTRING+"\n") #writing newString on the created file line by line
file2.close() #close the created file2
file1.close() #close opened file1



################################################################################
# Please do not edit anything below this line.
evaluate_lab7()

##################### End of the programme #####################################

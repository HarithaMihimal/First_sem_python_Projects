The Fibonacci sequence is defined with an integer n as,

    F(n) =F(n-1)+ F(n -2) for n >= 2, where F(0) =0 ,F(1)=1. 

You have to develop a Python program to compute F(n) for a given integer between 0 and 20. 

Input range:
0<= n <=20
 

Output range:
F(n)<=2^32




Compute F(n) starting with n=2 and increment iteratively until the required value is obtained. Follow the instructions below.

Create a text file containing the value of n. The text file needs to be saved in the same folder where the source file has been saved. The file name will be given as input through the terminal.
Develop a Python function named getNum to read the number n from the file.
Develop a Python function named show to display the given value n and the computed value of F(n) on the screen.
Expected output format: Fibonacci(3) = 2
Develop a Python function named saveFile to write what was displayed in (3) above to a text file named result.txt. This file should be in the same folder where the source file is.
The program should call the appropriate functions to achieve the task.
Print Invalid input. for values of n beyond the input range or other incompatible values.

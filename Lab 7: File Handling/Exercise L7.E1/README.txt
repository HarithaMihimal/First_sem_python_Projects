Develop a program to read the name, birthday, and gender of a person from a file and output the ten-digit national identity card (NIC) number.  The only input to the program is the name of the file.

The first four digits of the ID card are the birth year and the next three digits are the number of days to the birth date from January 1st of that year.
eg : Jan 1st - 1, Jan 2nd - 2, ...... , Feb 1st - 32, ......
If the person is a female, 500 is added to that value.
The next 3 digits are assigned in the order of submission for a particular birth year
The input file contains the records in the order of submission where each attribute is space-separated.

Example:

Contents of the input file	  
    Saman 1990-05-03 M
    Aruni 1990-04-06 F
    Kumaran 1988-03-05 M
    Nazar 1997-09-24 M
Contents of the expected output file
    Saman 1990123001
    Aruni 1990596002
    Kumaran 1988065001
    Nazar 1997267001

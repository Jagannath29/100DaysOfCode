# Steps to calculate execuation time of any program 

# a. First, store the time of initiation of the program into a variable
# b. Write the Python program
# c. Store the end time of the program into a variable
# d. Subtract the time of initiation of the program from the end time of the program



# importing modules

from time import time

start_time = time()

# Python program to create acronyms

sentence = 'Jhon likes going out'
text = sentence.split()

a = ''
for i in text:
    # takes first letter of each word in my sentence and make it upper
    a = a + str(i[0]).upper()

print(a)

end_time = time()

execution_time = end_time - start_time

print(f"Execution time is {execution_time}")
##2. Write a python program that asks the user for the name of a file, 
#and then repeatedly asks the user to enter a number, entering the number ‘0’ when finished. 
# Output each of these numbers to the file on a separate line.

outFileName = input("What is the name of your output file? ")
user_input = input("Please enter a number. Enter 0 when done: ")
dataFile = open(outFileName, "w") # create a new file to write on

while user_input != "0":
    print(user_input, file=dataFile) #file= (file destination)
    user_input = input("Please enter a number. Enter 0 when done: ") 
    # re-evaluate (assign each new) input to the same variable so it can be reused

dataFile.close()
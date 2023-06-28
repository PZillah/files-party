##2. Write a python program that asks the user for the name of a file, 
#and then repeatedly asks the user to enter a number, entering the number ‘0’ when finished. 
# Output each of these numbers to the file on a separate line.

PROMPT = "Please enter a number. Enter 0 when done: "

outFileName = input("What is the name of your output file? ")

dataFile = open(outFileName, "w") # create a new file

while input(PROMPT) != "0":
    userinput = input(PROMPT)
    print(userinput, file=dataFile)

dataFile.close()

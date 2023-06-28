# Read in a file called add.txt & display it to the screen
# Make sure add.txt is in the same project

dataFile = open("add.txt")
for line in dataFile: # read as: for each line in the file: do something
    print(line) # a line (of type str) from the file includeds \n new line
    #print(line.rstrip()) #removes extra line in btwn printed lines
dataFile.close()


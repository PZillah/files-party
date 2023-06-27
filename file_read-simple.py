# Read in a file called add.txt & display it to the screen
# Make sure add.txt is in the same project

dataFile = open("add.txt")
for line in dataFile:
    print(line.rstrip())
dataFile.close()


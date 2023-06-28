## Writing Files Practice
#1. Write a python program that reads in a text file and prints all the lines back out with a dash in front.

dataFile = open("read_file_txt.txt")
for line in dataFile:
    print(("-" + line).strip())
dataFile.close()
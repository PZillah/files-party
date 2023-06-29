##3. Write a python program that reads 3 files called text1.txt, text2.txt, and text3.txt, 
# counts the number of lines in each file, 
# and prints out the number of lines to a file counts.txt. 

dataFiles = ["text1.txt", "text2.txt", "text3.txt"]
outputFile = open("counts.txt", "w")

for file in dataFiles:
    count = sum(1 for line in open(file))
    print(file, ":", count, file=outputFile) # file=outputFile means the file destination
    
outputFile.close()
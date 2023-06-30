##4. Create a program similar to read3_files.py that counts the number of words in the files as well. 
# After printing out information about each file, this program should also print the total number of lines & words in all 3 files. 
# You can use the string split function to split a line of input into a list of words by splitting the line on spaces.

dataFiles = ["text1.txt", "text2.txt", "text3.txt"]
outputFile = open("counts.txt", "w")
total_line_count = 0 # aggregator variable
total_word_count = 0 # aggregator variable

for file in dataFiles:                          # for each file in the list of files,
    line_count = len(open(file).readlines())    # OR line_count = sum(1 for line in open(file)) # count the number of lines in each file
    total_line_count += line_count              # calculate total of lines for each file
    word_count = 0
    for line in open(file):                     # for every line in each file,
        lines = line.split()                    # split the lines into list of words
        word_count += len(lines)                # count the words in each line
        total_word_count += len(lines)          # calculate running total of words in each line
    print(file, ":", line_count, "lines,", word_count, "words", file=outputFile)

print("TOTAL: ", total_line_count, "lines,", total_word_count, "words", file=outputFile)
    
outputFile.close()
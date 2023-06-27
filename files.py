# Practice with files and dictionaries
# Count the number of letter grades in a file using a dictionary

letters = ["A", "B", "C", "D", "F"]
counts = {} # initialize a dictionary with {}
file = "letter-grades.txt" # open this file

#loop thru all lines in the file
for line in open(file):
    print(line)


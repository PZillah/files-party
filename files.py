# Practice with files and dictionaries
# Count the number of letter grades in a file using a dictionary

letters = ["A", "B", "C", "D", "F"]
counts = {} # initialize an empty dictionary with {}
file = "letter-grades.txt" # open this file

#loop thru all lines in the file
for line in open(file):
    letter = line.replace("\n", "") # replace blank line with nothing so there's no line space between each letter grade.
    # if there are commas, use split()
    # print(line) # for testing.
    count = counts.get(letter, 0) # gets the count of letter if it exists, 0 otherwise.
    counts[letter] = count + 1 # store that count into the dict

# Print out counts
print("Letter counts: ")
for letter in letters:
    print(letter + ":", counts.get(letter, 0))

# If you're just counting everything in a file and not worry about what's not there. Print out dictionary like so:
print("Grade counts dictionary:")
for item in counts.keys():
    print(item + ":", counts[item])

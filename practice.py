# Data project practice
# Write a program that reads in the sample_grades file and outputs the mean, median, and standard deviation 
# for the fall & spring semesters. Make sure to write at least two functions in your final solution. 
# The more generalizable you make your code, the more you may be able to reuse it for your own project later.

# 1st task: read in the data file and print it out to confirm it's working
# 2nd task: import to take advantage of built-in python functions for mean, median, standard deviation.
# 3rd task: need to split the data into an array
# 4th task: need to convert 3rd column of scores strings into an integer
# 5th task: print out something that looks like the sample output
# 6th task: make a function that calculates the mean, median and std.
# 7th task: write another function

import statistics

# Make a function
def get_stats(list):
   print("Mean:   ", statistics.mean(list))
   print("Median: ", statistics.median(list))
   print("STD:    ", statistics.stdev(list))

def show_stats():
    print("Fall 2016:")
    get_stats(fall)
    print()
    print("Spring 2016:")
    get_stats(spring)

# Data variables
spring = []
fall = []

# Read in the file
csv = "sample_grades.csv"
file = open(csv)

for line in file:
    # print(line.rstrip()) # remove white space to the right
    list = line.rstrip().split(",") # split() returns a list.
    # print(list)
    if list[1] == "Spring 2016":
        spring.append(eval(list[2]))
    else:
        fall.append(eval(list[2]))

file.close()

# print("Spring: ", spring)
# print("Fall:   ", fall)
# print("Fall 2016:")
# get_stats(fall)
# print()
# print("Spring 2016:")
# get_stats(spring)

show_stats()
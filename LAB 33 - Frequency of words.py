from itertools import count
file =open("course.txt" ,"r")
count = 0
for line in file:
    words =line.split(" ")
    count +=len(words)
file.close()
print("Number of words in a text file:", count)

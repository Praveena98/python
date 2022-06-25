import random
file =open("course.txt" ,"r")
line = file.readlines()
length =len(line)
r =random.randint(0,length-1)
print(line[r])
file.close()


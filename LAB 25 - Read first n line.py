n = int(input("Enter n lines:-"))
f=open("course.txt","r")
for line in(f.readlines()[0:n]):
    print(line,end="")
f.close()

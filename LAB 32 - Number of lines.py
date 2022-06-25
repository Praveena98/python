def countline():
    file =open("course.txt","r")
    line =file.readlines()
    c =0
    for i in line:
        c=c+1
    print("Total number of lines:" ,c)
    file.close()
countline()

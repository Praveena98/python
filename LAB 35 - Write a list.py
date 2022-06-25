a_list = ["HTML", "CSS", "BOOTSTRAP","JAVASCRIPT","MYSQL","PYTHON"]
textfile = open("LAB35.txt", "w")
for element in a_list:
    textfile.write(element + "\n")
textfile.close()

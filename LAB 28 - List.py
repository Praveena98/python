with open ("course.txt")as f:
   content_list= f.readlines()
#Print the list
print(content_list)  
#remove new line characters
content_list =[x.strip() for x in content_list]
print(content_list)

givenFilename = "course.txt"
with open(givenFilename, 'r') as givenfilecontent:
        lines_lst= givenfilecontent.readlines()
print([a.rstrip('\n') for a in lines_lst])

from fileinput import filename
import os
def getfileSize(filename):
    return os.stat(filename).st_size
filename = input("Enter a file name:")
size = getfileSize(filename)
print("Filesize:-", size)

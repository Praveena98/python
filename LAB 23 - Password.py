import random
import string
from symtable import Symbol
length =int(input("\n Enter the length of password:"))
lower =string.ascii_lowercase
upper =string.ascii_uppercase
num = string.digits
symbol =string.punctuation
all=  lower +upper+num+symbol
temp =random.sample(all,length)
password = " ".join(temp)
print("unique password : ", password)
import datetime
name=input("Enter your name:-")
age=int(input("Enter your age:-"))
currentyear= datetime.datetime.now().year
dob =currentyear -age
hundredth_year =dob+100
print (f'{name} will become 100 year old in the year {hundredth_year}')
n =int(input("Enter an number: "))
list1 =list(range(2,n+1))   # list compreshion 
answer =[ ]
for number in list1:
       if n% number ==0:
           answer.append(number)
print(f'{n} is fully divisible by {answer}')




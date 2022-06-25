import random
random_number = random.randint(1,9)
guessed_number =int(input("Enter a number between 1 an 9:-"))
while guessed_number is not random_number:
    if(guessed_number <random_number):
        print("You have to guessed high")
    else:
        print("You have to guessed low")
    guessed_number =int(input("Enter a number between 1 an 9:-"))
print("your guess is correct ") 
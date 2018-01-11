# Charles Buyas cjb8qf


import random
print("Input a -1 to play with a random number")
start = int(input("What should the answer be?: "))
count = 0
if start == -1:
    start = random.randint(1, 100)
else:
    num = start

while count < 4:
    guess = int(input("Guess a number: "))
    if int(guess) == int(start):
        print("You win!")
        exit(0)
    elif int(guess) > int(start):
        count += 1
        print("The number is lower than that.")
    else:
        count += 1
        print("The number is higher than that.")

if count == 4:
    guess = int(input("Guess a number: "))
    if int(guess) == int(start):
        print("You win!")
        exit(0)
    else:
        print("You lose; the number was " + str(start) + ".")

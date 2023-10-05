import random

num=random.randint(1,20)

while True:
    guess=int(input("Guess A number between 1 to 20 :"))

    if guess==num:
        print("You Guessed A Correct Number")
    if guess>num:
        print("You Guessed A Greater Number")
    if guess<num:
        print("You Guessed A Smaller Number")

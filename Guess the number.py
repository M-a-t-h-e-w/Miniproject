import random

guess  = int(input("Guess the Number:"))
r=random.randint(1,50)
while guess > r:
    print("The number is 50 more than the limit :(")
    break

while True:
    if guess < r:
        print("You have guessed small number :)")
        guess = int(input("Guess the Number:"))

    elif guess > r:
        print("You have guessed big number :(")
        guess = int(input("Guess the Number:"))

    elif guess == r:
        print("congratulation :) you have guessed correct Number")
        break


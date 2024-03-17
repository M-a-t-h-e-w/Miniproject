import random

print("Welcome to the Game Rock/paper/scissor :) ")
option = ["rock","paper","scissor"]
user = 0
Ai = 0

while True:
    user_input = input("Type Rock paper or scissor or YOu can quite by entering q :)").lower()
    if user_input == "q":
        break

    if user_input not in option:
        continue

    random_number = random.randint(0,2)
    computer = option[random_number]

    if user_input == "rock" and computer == "scissor":
        print("You won")
        user += 1
    elif user_input == "paper" and  computer == "rock":
        print("You won")
        user += 1
    elif user_input == "scissor" and computer == "paper":
        print("You won")
        user += 1
        break
    if user_input == "scissor" and computer == "rock":
        print("computer won")
        Ai += 1
    elif user_input == "rock" and  computer == "paper":
        print("computer won")
        Ai += 1
    elif user_input == "paper" and computer == "scissor":
        print("computer won")
        Ai += 1
        break
print("Game is ended Bye :)")
print("User score",user)
print("computer score",Ai)
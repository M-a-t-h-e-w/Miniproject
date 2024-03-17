
print("Welcome to my Quizze Game")
player = input("Do you want to play the Game? ")
if player.lower() != "yes":
    quit()
print("Ok least Start the Game :)")
score = 0
answer1 = input("What is CPU Stand for? ")
if answer1.lower() == "central processing unit":
    print("Correct answer:)")
    score += 1
else:
    print("wrong answer :(")
answer3 = input("What is RAM Stand for? ")
if answer3.lower() == "random access memory":
    print("Correct answer:)")
    score += 1
else:
    print("wrong answer :(")
answer2 = input("What is ROM Stand for? ")
if answer2.lower() == "read only memory":
    print("Correct answer:)")
    score += 1
else:
    print("wrong answer :(")

answer2 = input("How aplhabet are there in English? ")
if answer2.lower() == "26":
    print("Correct answer:)")
    score += 1
else:
    print("wrong answer :(")

answer2 = input("What is CCN stands for? ")
if answer2.lower() == "Content-Centric Networking":
    print("Correct answer:)")
    score += 1
else:
    print("wrong answer :(")


print("This is your percentage",(score / 4 * 100),"%.")
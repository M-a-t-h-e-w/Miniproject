print("Hello, Welcome to cave adventure game!")
print()
answer = input("Are you interested in exploring cave (Yes/no) :) ").lower()
print()
if answer == "yes":
    print("We are taking you to the cave ")
    print()
elif answer == "no":
    print("You are return :(")
    quit(answer)


answer = input("Do you wanted to get inside the cave :)  (yes/no)?").lower()
if answer == "yes":
    print("Cave is really very dangerous so plz note the hole and walk patiently ")
    print()
elif answer == "no":
    print("you have return :(")
    quit(answer)

answer=input("Do you scared of entering inside the cave (yes/no)").lower()
print()
if answer == "yes":
    print("you have return :(")
    quit(answer)
elif answer == "no":


    answer = input("Ok Lets go deeper into it and explore :) In the cave some of int will be writen in the rocks, if you don't answer correct  you will remain inside the cave or if your answer is correct you can exit from the cave! (Enter Ok!)")
if answer == "ok":
    print()


answer = input(" The int (5 multiple by 24)")
if answer == "120":
    print("you have answed correct, you get out of the cave :)")
else:
    print("You have answed wrong, so you lose :(")

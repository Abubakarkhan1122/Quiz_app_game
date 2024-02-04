print("Welcome to the Quiz Game")
play_game = input(" would you like to play a game of Quiz? ")
if play_game != "yes":
    print("Type 'yes' to play")
else:
    print(" play a game of Quiz")

score = 0
answer = input("what does RAM stands for ")
if answer.lower() == "random access memory":
        print("Correct!")
        score=+1

else:
    print("Wrong!")
answer = input("what does ROM stands for ")
if answer.lower() == "read only memory":
        print("Correct!")
        score = +1

else:
        print("Wrong!")
answer = input("what does CPU stands for ")
if answer.lower() == "central processing unit":
            print("Correct!")
            score = +1

else:
            print("Wrong!")

answer = input("what does AI stands for ")
if answer.lower() == "Artifical intelligence":
                print("Correct")
                score = +1
else:
                print("Wrong!")

answer = input("guess the logo of iphone ")
if answer.lower() == "apple":
                    print("Correct")
                    score = +1
else:
                    print("Wrong!")
                    print("you gain "+str((score/5 )* 100)+" points")

print("thank you for playing")
print("**********")

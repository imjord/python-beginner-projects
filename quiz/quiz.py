print("Quiz Game in Python")


# prompt user for input
playing = input("Do you want to play? ")

if(playing.lower() != "yes"):
    quit()

print("time to play")
score = 0

question = input("Are you awesome?")
if(question.lower() != "yes"):
    print("You lost points!")
    score -=1
else: 
    score += 1
    print("Good job on question 1!")
question = input("whats 2 + 2")
if(question != "4"):
    print("You lost points!")
    score -=1
else: 
    score += 1
    print("Good job on question 2!")
question = input("Whats 5 + 5")
if(question != "10"):
    print("You lost points!")
    score -=1
else: 
    score += 1
    print("Good job on question 3!")

print("Your score is ", str(score), "Good job")
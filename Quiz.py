print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is a nadir? ")
if answer.lower() == "bottom vanishing point":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What's 10+10? ")
if answer.lower() == "20":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the president of America? ")
if answer.lower() == "joe biden":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

print("You got " + str(score) + "questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

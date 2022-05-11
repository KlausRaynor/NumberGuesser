# Code by Jose Lizama & Klaus Holder
import random
# declare answer
correctAnswer = random.randrange(0,100)
# declare starting score
score = 100
print("correct answer is ", correctAnswer)
# ask name
name = input("What is your name?\n")
# print introduction
print("Whatup, " + name + "!")

# initialize
userGuess = -1
# create guessCheck function
# takes userGuess
# compare to correctAnswer
# if guess is wrong:
# If number is higher, print "Wrong, number is higher" & subtract 5 pts from score
# If number is lower, print "Wrong, number is lower" & subtract 5 pts from score
# if number is correct, print "You got it! Your final score is: " + score
def guessChecker (score, correctAnswer, userGuess):
    userGuess = int(print("Try to guess the number between 1 and 100"))
    while userGuess != correctAnswer:
        try:
        elif userGuess < correctAnswer:
            score -= 5
            print("You guessed too low, try again!")
            userGuess = input("Your guess is: ")
        else:
            print("You got it! Your final score is: ", score)

guessChecker(int(score), int(correctAnswer), int(userGuess))

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break
if age >= 18:
    print("You are able to vote in the United States!")
else:
    print("You are not able to vote in the United States.")
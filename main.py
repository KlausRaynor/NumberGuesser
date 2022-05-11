#Code by Jose Lizama & Klaus Holder
import random

def intro():
    #declare answer
    CORRECT_ANSWER = random.randrange(0,100)

    #declare starting score
    score = 100

    #flags if player has won(true) or not won(false)
    winFlag = False

    print("WELCOME TO THE NUMBER GUESSING GAME!\n Start by inputting your name, and then guess numbers between 1 and 100.\n"
          "You will get a hint as to whether it is too high or too low.")

    name = input("What is your name?\n")
    #print introduction
    print("Whatup, " + name + "!")
    userGuess = -1
    guessChecker(score, CORRECT_ANSWER, userGuess, name)
def win(s):
    print("Congratulations! You win! Your final score is: ", s,". Do you want to play again?")
    goAgain = input()
    startOver(goAgain)

def startOver(goAgain):
    if goAgain == "Y":
        intro()
    elif goAgain =="N":
        print("Thank you for playing!\n Have a nice day.")
        exit

def guessChecker(score, correctAnswer, userGuess, name):
    print("Try to guess the number between 1 and 100")
    userGuess = int(input("Your guess is: "))
    if userGuess != correctAnswer:
        while userGuess != correctAnswer:
                if userGuess > correctAnswer:
                    score -= 5
                    print("I'm sorry, your guess was too high. Your score is now: ", score)
                    userGuess = int(input("Guess again! Your guess: "))
                elif userGuess < correctAnswer:
                    score -= 5
                    print("I'm sorry, your guess was too low. Your score is now: ", score)
                    userGuess = int(input("Guess again! Your guess: "))
    win(score)


intro()


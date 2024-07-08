import random

def guessNumber():
    guess = random.randint(0,100)

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 0 and 100!")
    difficulty = input("Choose a difficulty! Easy or Hard: ").lower()

    if difficulty == "easy":
        noGuesses = 10
        print(f"You have {noGuesses} attempts to guess the number!")

        while noGuesses > 0:
            
            userGuess = int(input("What is your guess?: "))        
            
            if userGuess > guess:
                print(f"Your guess {userGuess} is higher than the number!")
                noGuesses -= 1
                print(f"You have {noGuesses} guesses left!")
            elif userGuess < guess:
                print(f"Your guess {userGuess} is lower than the number!")
                noGuesses -= 1
                print(f"You have {noGuesses} guesses left!")
            elif userGuess == guess:
                print(f"Your guess {userGuess} is the chosen number, you win!")
                break

        if noGuesses == 0:
            print(f"You lose!, the answer was {guess}")

    else:
        noGuesses = 5
        print(f"You have {noGuesses} attempts to guess the number!")

        while noGuesses > 0:
            
            userGuess = int(input("What is your guess?: "))        
            
            if userGuess > guess:
                print(f"Your guess {userGuess} is higher than the number!")
                noGuesses -= 1
                print(f"You have {noGuesses} guesses left!")
            elif userGuess < guess:
                print(f"Your guess {userGuess} is lower than the number!")
                noGuesses -= 1
                print(f"You have {noGuesses} guesses left!")
            elif userGuess == guess:
                print(f"Your guess {userGuess} is the chosen number, you win!")
                break

        if noGuesses == 0:
            print(f"You lose!, the answer was {guess}")

guessNumber()
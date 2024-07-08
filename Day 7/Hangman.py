import random
from wordList import word_list

wordList = word_list

endOfGame = False
chosenWord = random.choice(wordList)
lives = 6

display = []

for i in chosenWord:
    display.append("_")

print(display)

while "_" in display:

    guess = input("Guess a letter: ").lower()
    
    if guess in chosenWord:
        if guess in display:
            print("You have already chose this letter!")
        else:
            for i in range(len(chosenWord)):
                if chosenWord[i] == guess:
                    display[i] = guess
    else:
        lives -= 1
        print(f"You have {lives} lives left!")
            
    if lives == 0:
        print("You lose!")
        print(f"The word was {chosenWord}")
        break
        
    if "_" not in display:
        endOfGame = True
        print("You Win!")
        break

    print(display)


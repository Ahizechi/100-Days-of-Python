import random

game = input("Do you want to play a game of Blackjack? Type 'Yes' or 'No': ").lower()

cardChoices = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

cardValues = {
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "10": 10,
    "Jack": 10, 
    "Queen": 10, 
    "King": 10,
    "Ace": 1
}

userChoice = random.sample(cardChoices, 2)
userCard = userChoice

print(f"Your cards: {userCard}")

compCard = []
compChoice = random.choice(cardChoices)
compCard.append(compChoice)
print(f"Computer's first card: {compChoice}")

draw = input("Would you like to draw another card? Type 'Yes' or 'No': ").lower()

if draw == "yes":
    lastCard = random.choice(cardChoices)
    userCard.append(lastCard)

print(f"Your final hand: {userCard}")

compChoiceTwo = random.choice(cardChoices)
compCard.append(compChoiceTwo)
print(f"Computer now has: {compCard}")

compSumCalc = []

for value in compCard:
    individualValue = cardValues[value]
    compSumCalc.append(individualValue)

if sum(compSumCalc) < 17:
    print("Computer must draw one more card!")
    compChoiceThree = random.choice(cardChoices)
    compCard.append(compChoiceThree)
    
print(f"The computer's final hand is: {compCard}")
print(f"Your final hand: {userCard}")

finalUserCalc = []
finalCompCalc = []

for x in userCard:
    individualCount = cardValues[x]
    finalUserCalc.append(individualCount)

for y in compCard:
    individualCountComp = cardValues[y]
    finalCompCalc.append(individualCountComp)

sumUser = sum(finalUserCalc)
sumComp = sum(finalCompCalc)
totalBoth = sumComp + sumUser

if sumUser > 21:
    print("You Lose!")
elif sumComp > 21 and sumUser < 22:
    print("You win!")
elif sumUser > sumComp and totalBoth < 43:
    print("You win!")
elif sumUser < sumComp and totalBoth < 43:
    print("You Lose!")
elif sumComp == sumUser and totalBoth < 43:
    print("Draw!")



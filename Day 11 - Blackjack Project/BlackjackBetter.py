import random

def play_blackjack():
    game = input("Do you want to play a game of Blackjack? Type 'Yes' or 'No': ").lower()
    if game != 'yes':
        print("Maybe next time!")
        return

    cardChoices = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    cardValues = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "Jack": 10, "Queen": 10, "King": 10, "Ace": 1  # Simplified Ace handling
    }

    userCard = random.sample(cardChoices, 2)
    compCard = random.sample(cardChoices, 2)
    print(f"Your cards: {userCard}, Computer's first card: {compCard[0]}")

    if input("Would you like to draw another card? Type 'Yes' or 'No': ").lower() == "yes":
        userCard.append(random.choice(cardChoices))
    print(f"Your final hand: {userCard}")

    while sum(cardValues[card] for card in compCard) < 17:
        compCard.append(random.choice(cardChoices))

    print(f"The computer's final hand is: {compCard}")

    sumUser = sum(cardValues[card] for card in userCard)
    sumComp = sum(cardValues[card] for card in compCard)

    if sumUser > 21:
        print("You Lose!")
    elif sumComp > 21:
        print("You Win!")
    elif sumUser > sumComp:
        print("You Win!")
    elif sumUser < sumComp:
        print("You Lose!")
    else:
        print("Draw!")

play_blackjack()

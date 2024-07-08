import random

numberYOU = random.randint(0,1)
numberTHEM = random.randint(0,1)

if numberYOU > 0.5 and numberTHEM < 0.5:
    print("You picked heads, they picked tails, you win!")
elif numberTHEM > 0.5 and numberYOU < 0.5:
    print("You picked tails, they picked heads, you lose!")
elif numberTHEM > 0.5 and numberYOU > 0.5:
    print("You both picked heads, its a draw!")
else:
    print("You both picked tails, its a draw!")

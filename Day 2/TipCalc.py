print("Welcome to the tip calculator!")

total = int(input("How much was the bill?"))
tip = int(input("How much would you like to tip? 10,12 or 15?"))


if tip not in (10, 12, 15):
    print("Not a valid tip amount!")
else:
    if tip == 10:
        amount = total * 0.1
        billSpilt = int(input("How many people are splitting the bill?"))
        totalEach = amount / billSpilt
        totalEach = round(totalEach, 2)
        print(f"Each person should pay {totalEach}")
    if tip == 12:
        amount = total * 0.12
        billSpilt = int(input("How many people are splitting the bill?"))
        totalEach = amount / billSpilt
        totalEach = round(totalEach, 2)
        print(f"Each person should pay {totalEach}")
    if tip == 15:
        amount = total * 0.15
        billSpilt = int(input("How many people are splitting the bill?"))
        totalEach = amount / billSpilt
        totalEach = round(totalEach, 2)
        print(f"Each person should pay {totalEach}")

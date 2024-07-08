print("Welcome to the Auction Program!")

bids = {}

def auction():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    other = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()

    bids[name] = bid

    if other == "yes":
        auction()


auction()
nameWinner = max(bids, key=bids.get) # will output the highest number
maxValue = bids[nameWinner]
print(f"Congrats! {nameWinner} won the auction with a bid of ${maxValue}!")
print(bids)


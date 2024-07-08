import random

def get_two_celebrities(celebs):
    return random.sample(list(celebs.keys()), 2)

def play_round(celebs):
    celeb1, celeb2 = get_two_celebrities(celebs)
    print(f"Who has more Instagram followers? A: {celeb1} or B: {celeb2}")
    guess = input("Choose A or B: ")
    correct_answer = 'A' if celebs[celeb1] > celebs[celeb2] else 'B'
    if guess.upper() == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Wrong! {correct_answer} ({celeb1 if correct_answer == 'A' else celeb2}) has more.")
        return 0

def main():
    instagram_followers = {
        "Cristiano Ronaldo": 562000000,
        "Kylie Jenner": 400000000,
        "Lionel Messi": 450000000,
        "Selena Gomez": 380000000,
        "Dwayne Johnson": 360000000,
        "Ariana Grande": 350000000,
        "Kim Kardashian": 340000000,
        "Beyoncé": 290000000,
        "Khloe Kardashian": 280000000,
        "Kendall Jenner": 270000000,
        "Justin Bieber": 260000000,
        "National Geographic": 250000000,
        "Taylor Swift": 240000000,
        "Jennifer Lopez": 230000000,
        "Neymar": 200000000,
        "Nicki Minaj": 190000000,
        "Miley Cyrus": 180000000,
        "Katy Perry": 170000000,
        "Kourtney Kardashian": 160000000,
        "Kevin Hart": 150000000
    }

    score = 0
    play = True
    while play:
        score += play_round(instagram_followers)
        print(f"Current score: {score}")
        if input("Play another round? (yes/no): ").lower() != 'yes':
            play = False
    print(f"Final score: {score}")

if __name__ == "__main__":
    main()
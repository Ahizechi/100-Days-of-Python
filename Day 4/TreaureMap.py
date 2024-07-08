line1 = ["_", "_", "_"]
line2 = ["_", "_", "_"]
line3 = ["_", "_", "_"]

map = [line1, line2, line3]
print("Hiding your treasure, X marks the spot!")
position = input()

letter = position[0].lower()
abc = ["a", "b", "c"]
letterIndex = abc.index(letter)
number = int(position[1]) - 1
map[number][letterIndex] = "X"

print(f"{line1}\n{line2}\n{line3}")
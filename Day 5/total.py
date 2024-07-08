total = 0

for i in range(0,11):
    total += i
    
print(total)

totalEven = 0
target = int(input("What number?: "))

for x in range(0,target + 1,2):
    totalEven += x
    
print(totalEven)
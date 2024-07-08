# def primeCheck(number):
#     if number == 1:
#         print("This is NOT a prime number! 1")
    
#     i = 2
#     while i <= number:
#         if number % i == 0 and i != number:
#             print(f"This is NOT a prime number! {number}")
#             break
#         else:
#             if number == number:
#                 print("This is a prime number!")
#                 break
#             else:
#                 i += 1

            

# number = int(input("What number? "))
# primeCheck(number)

def primeCheck(number):
    if number <= 1:
        print(f"This is NOT a prime number! {number}")
        return
    i = 2
    while i < number:
        if number % i == 0:
            print(f"This is NOT a prime number! {number}")
            return
        i += 1
    print("This is a prime number!")

number = int(input("What number? "))
primeCheck(number)

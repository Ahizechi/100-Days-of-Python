import math

def calcPaint(height, width):
    meters = height * width
    paintNeeded = meters / 5
    paintTotal = math.ceil(paintNeeded)
    print(paintTotal)

calcPaint(60, 60)
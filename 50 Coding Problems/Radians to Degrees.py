import math

#pi = float(math.pi())

def radiansToDegrees(x):
    if x == int or float:
        x = float(x)
        degrees = (x*math.pi) * (180/math.pi)
        print(degrees)
        radiansToDegrees(input('Please input a Radian to convert into Degrees. The pi symbol will be added to the end. (only takes numbers)   '))
    else:
        radiansToDegrees(float(input('That is not a number. ---Please input a Radian to convert into Degrees. The pi symbol will be added to the end. (only takes numbers)   ')))

radiansToDegrees(input('Please input a Radian to convert into Degrees. The pi symbol will be added to the end. (only takes numbers)   '))

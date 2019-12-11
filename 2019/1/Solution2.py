import math as math

intCodeFile = open('intCode.txt')
#intCodeFile = open('testintCode.txt')
intCode = intCodeFile.readlines()

result = 0

def calcFuelNeeds(mass):
    return math.floor(mass/3) - 2

for line in intCode:
    while True:
        subResult = calcFuelNeeds(int(line))
        print(subResult)
        if subResult > 0:
            result += subResult
            line = subResult
        else:
            break

print("Final result: ", result)
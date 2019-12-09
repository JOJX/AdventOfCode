import math as math

inputFile = open('input.txt')
#inputFile = open('testInput.txt')
input = inputFile.readlines()

result = 0

def calcFuelNeeds(mass):
    return math.floor(mass/3) - 2

for line in input:
    while True:
        subResult = calcFuelNeeds(int(line))
        print(subResult)
        if subResult > 0:
            result += subResult
            line = subResult
        else:
            break

print("Final result: ", result)
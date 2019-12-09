import math as math

inputFile = open('input.txt')
#inputFile = open('testInput.txt')
input = inputFile.readlines()

result = 0

for line in input:
    subResult = math.floor(int(line)/3) - 2
    print(subResult)
    result += subResult

print("Final result: ", result)

import math as math

intCodeFile = open('intCode.txt')
#intCodeFile = open('testintCode.txt')
intCode = intCodeFile.readlines()

result = 0

for line in intCode:
    subResult = math.floor(int(line)/3) - 2
    print(subResult)
    result += subResult

print("Final result: ", result)

intCode = []
goal = 19690720

def loadintCode():
    intCode.clear()
    with open('intCode.txt') as intCodeFile:
       for line in intCodeFile:
            for el in line.split(','):
                intCode.append(int(el))

def executeOpCode(position):
    if intCode[position] == 1:
        intCode[intCode[position+3]] = intCode[intCode[position+1]] + intCode[intCode[position+2]]
    elif intCode[position] == 2:
        intCode[intCode[position+3]] = intCode[intCode[position+1]] * intCode[intCode[position+2]]

loadintCode()

for noun in range(0,100,1):
    if intCode[0] == goal:
        break
    for verb in range(0,100,1):
        if intCode[0] == goal:
            break
        loadintCode()
        intCode[1] = noun
        intCode[2] = verb

        for i in range(0, len(intCode), 4):
            if intCode[i] == 1 or intCode[i] == 2:
                executeOpCode(i)
            elif intCode[i] == 99:
                if intCode[0] == goal:
                    print("The answer is ", 100*noun+verb)
                    break
                break
            else:
                print("Encountering an unknown opcode means something went wrong")


intCode = []
with open('intCode.txt') as intCodeFile:
   for line in intCodeFile:
        for el in line.split(','):
            intCode.append(int(el))

def executeOpCode(position):
    if intCode[position] == 1:
        intCode[intCode[position+3]] = intCode[intCode[position+1]] + intCode[intCode[position+2]]
    elif intCode[position] == 2:
        intCode[intCode[position+3]] = intCode[intCode[position+1]] * intCode[intCode[position+2]]

for i in range(0, len(intCode), 4):
    if intCode[i] == 1 or intCode[i] == 2:
        executeOpCode(i)
    elif intCode[i] == 99:
        print("DONE")
        break
    else:
        print("Encountering an unknown opcode means something went wrong")

print("Final result: ", intCode)

input = []
goal = 19690720

def loadInput():
    input.clear()
    with open('input.txt') as inputFile:
       for line in inputFile:
            for el in line.split(','):
                input.append(int(el))

def executeOpCode(position):
    if input[position] == 1:
        input[input[position+3]] = input[input[position+1]] + input[input[position+2]]
    elif input[position] == 2:
        input[input[position+3]] = input[input[position+1]] * input[input[position+2]]

loadInput()

for noun in range(0,100,1):
    if input[0] == goal:
        break
    for verb in range(0,100,1):
        if input[0] == goal:
            break
        loadInput()
        input[1] = noun
        input[2] = verb

        for i in range(0, len(input), 4):
            if input[i] == 1 or input[i] == 2:
                executeOpCode(i)
            elif input[i] == 99:
                if input[0] == goal:
                    print("The answer is ", 100*noun+verb)
                    break
                break
            else:
                print("Encountering an unknown opcode means something went wrong")


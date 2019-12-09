input = []
with open('input.txt') as inputFile:
   for line in inputFile:
        for el in line.split(','):
            input.append(int(el))

def executeOpCode(position):
    if input[position] == 1:
        input[input[position+3]] = input[input[position+1]] + input[input[position+2]]
    elif input[position] == 2:
        input[input[position+3]] = input[input[position+1]] * input[input[position+2]]

for i in range(0, len(input), 4):
    if input[i] == 1 or input[i] == 2:
        executeOpCode(i)
    elif input[i] == 99:
        print("DONE")
        break
    else:
        print("Encountering an unknown opcode means something went wrong")

print("Final result: ", input)

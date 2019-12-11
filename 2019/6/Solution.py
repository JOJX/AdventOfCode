intCode = []
step = 2
with open('input.txt') as intCodeFile:
   for line in intCodeFile:
        for el in line.split(','):
            intCode.append(int(el))

#opcode - extracted OpCode to execute
#position - position in the whole IntCode  
#Parameter modes: 0-position mode(address), 1-Immediate mode(value)
def executeOpCode(opCode, position):
    instruction = int(opCode[0]) #First two signs are for instruction
    instrLen = 0
    paramAMode = 0
    paramBMode = 0

    #PREPARE PARAMETERS
    if len(opCode) == 4:
        paramAMode = int(opCode[2])
        paramBMode = int(opCode[3])
    elif len(opCode) == 3:
        paramAMode = int(opCode[2])

    if instruction != 3 and instruction != 4:
        if paramAMode: #Value mode
            paramA = intCode[position+1]
        else: #Address mode
            paramA = intCode[intCode[position+1]]
                
        if paramBMode: #Value mode
            paramB = intCode[position+2]
        else: #Address mode
            paramB = intCode[intCode[position+2]]
    elif instruction == 4:
        if paramAMode: #Value mode
            paramA = intCode[position+1]
        else: #Address mode
            paramA = intCode[intCode[position+1]]
                
    # END OF - PREPARE PARAMETERS
    ##############################################
    # EXECUTE INSTRUCTION:
    if instruction == 1: #Addition 
        instrLen = 4
        intCode[intCode[position+3]] = paramA + paramB

    elif instruction == 2: #Multiplication
        instrLen = 4
        intCode[intCode[position+3]] = paramA * paramB

    elif instruction == 3: #Input
        instrLen = 2
        intCode[intCode[position+1]] = int(input())

    elif instruction == 4: #Output
        instrLen = 2
        print(paramA)

    elif instruction == 5: #Jump if true
        if paramA:
            instrLen = paramB - position
        else:
            instrLen = 3

    elif instruction == 6: #Jump if false
        if paramA == 0:
            instrLen = paramB - position
        else:
            instrLen = 3

    elif instruction == 7: #Jump if less than
        if paramA < paramB:
            intCode[intCode[position+3]] = 1
        else:
            intCode[intCode[position+3]] = 0
        instrLen = 4

    elif instruction == 8: #Jump if equals
        if paramA == paramB:
            intCode[intCode[position+3]] = 1
        else:
            intCode[intCode[position+3]] = 0
        instrLen = 4

    else:
        instrLen = -1
        print("Unknown Instruction")
    
    return instrLen

pos=0
while pos < len(intCode):
    opCode = str(intCode[pos])
    opCode = opCode[::-1] #reverse string for easier extracting of parameters mode
    
    if opCode == '99':
        print("DONE")
        break
    else:
        instrLen = executeOpCode(opCode, pos)

    if instrLen>0:
        pos += instrLen
    else:
        break


print("I MEAN REALLY DONE")

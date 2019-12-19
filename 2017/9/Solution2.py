#Should return 10
testInput = "<{osi!a,<{i<a>"
result =0
#Prepare input as a list of custom class objects
with open('input.txt') as inputFile:  
   for line in inputFile:
        data = line

#data = testInput

#0 - GROUP, 1-GARBAGE
isGarbage = 0
score = 1
garbageCount = 0
dataIter = iter(data)
iterations = 0
dataLen = len(data)
for character in dataIter:
    iterations += 1
    # When in garbage block then wait for garbage end
    if isGarbage:
        # Skip chars when !
        if character == '!':
            next(dataIter, None)
            continue
        #End of garbage
        elif character == '>':
            isGarbage = 0
            continue
        else:
            garbageCount += 1
            continue
    #Regular group        
    else:
        #New group
        if character  == '{':
            result += score
            score += 1
        #End group
        elif character  == '}':
            score -= 1    
        #Skip char
        elif character  == '!':
            next(dataIter, None)
            continue 
        #Garbage block start
        elif character  == '<':
            isGarbage = 1
    
print("Solution: ",  garbageCount)
print("Data length: ",  dataLen,  "Iterations: ",  iterations)

import time
start = time.time()

with open('input.txt') as inputFile:  
    input = inputFile.readlines()

result = 0

for line in input:
    validChkSum = []
    lettersCount = [[], []]
    for i in range(0, len(line)):
        if line[i].isdigit():
            break
        if line[i] not  in lettersCount[0] and line[i].isalpha():
            lettersCount[0].append( line[i] ) 
            lettersCount[1].append( line.count(line[i]) )
    validChkSum.append( lettersCount[0][ lettersCount[1].index( max(lettersCount[1]) ) ]) 
    
print("Number of valid rooms: ",  result)

end = time.time()
print("Computation took: ",  end-start)

input = []
#For testing use testInput.txt file - answer should be 5
with open('input.txt') as inputFile:  
    for line in inputFile:
        input.append(int(line))

prevIndex = 0
index = 0
result = 0

while index < len(input):
    prevIndex=index
    index = index + input[index]
    input[prevIndex] +=1
    
    result+=1
    
print("Solution: ",  result)

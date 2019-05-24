import time
start = time.time()

inputData = []

with open('input.txt') as inputFile:  
    for line in inputFile:
        a, b, c = line.split()
        inputData.append((int(a), int(b), int(c)))
        

result = 0

#Check if triangle can be made out of this sides
def checkTriangle(triangle):
    a, b, c = triangle
    if (a+b > c):
        if (a+c > b):
            if (b+c > a):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
#Check how many triangles are valid
for triangle in inputData:
    if checkTriangle(triangle):
        result += 1
    
print("Number of valid triangles: ",  result)
end = time.time()
print("Computation took: ",  end-start)

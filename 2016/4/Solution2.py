import time
start = time.time()

#Same as Solution1 but data needs to preprocessed differently 
#101 301 501
#102 302 502
#103 303 503
#Now triangles sides are listed in columns instead of rows

inputData = []

with open('input.txt') as inputFile:  
    for i in range(0, 3):
        for line in inputFile:
            inputData.append(int(line.split()[i]))
        inputFile.seek(0)

result = 0

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
    
triangle = []
i = 0
for side in inputData:
    triangle.append(side)
    if len(triangle) == 3:
        if checkTriangle(triangle):
            result += 1
        triangle.clear()
            
    
print("Number of valid triangles: ",  result)
end = time.time()
print("Computation took: ",  end-start)

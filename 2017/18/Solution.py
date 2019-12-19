import time

start = time.time()

circBuffer = []
circBuffer.append(0)
currentPos = 0
nextPos = 0
stepSize = 371

def addToBuffer(pos, elem):
    global currentPos
    circBuffer.insert(pos,  elem)
    currentPos = pos
    
def findNextPos():
    return ((currentPos+stepSize) % len(circBuffer))+1 

for i in range(1, 2018):
    pos = findNextPos()
    addToBuffer(pos,  i)

end = time.time()
print("Took: ",  end-start)

#next element after 2017
print(circBuffer[circBuffer.index(2017)+1])

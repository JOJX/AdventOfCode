import time

start = time.time()

zeroPos = 0
nextValue=0
currentPos = 0
stepSize = 371

for i in range(1, 50000001):
    pos = ((currentPos+stepSize) % i)+1 
    
    if pos > zeroPos+1:
        pass
    elif pos <= zeroPos:
        zeroPos+=1
    elif pos == zeroPos+1:
        nextValue = i        
    
    currentPos = pos
    
#next element after 0
print(nextValue)

end = time.time()
print("Took: ",  end-start)

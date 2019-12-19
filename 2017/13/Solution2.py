import time

_depth = []
_range = []

with open('input.txt') as inputFile:  
   for line in inputFile:
        line  = line.replace(':',  '')
        input = line.split()
        _depth.append( int( input[0] ) )    
        _range.append( int( input[1] ) )

collision = []
i=0
delay = 10

start = time.time()

while True:
    collision.clear()
    i=0
    for step in _depth:
        if  (step+delay) % ( (_range[i]-1)*2) == 0:
            collision.append(step)
        i +=1
    if not len(collision):
        break
    delay += 1

end = time.time()
    
print(collision)
print("Result: ",  delay)

print("Took: ",  end - start)

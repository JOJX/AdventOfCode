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
result = 0

for step in _depth:
    if step == 0:
        collision.append(step)
        result += 0*_range[i]
    elif  step % ( (_range[i]-1)*2) == 0:
        collision.append(step)
        result += step*_range[i]
    i +=1
    
print(collision)
print(result)


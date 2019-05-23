import time
start = time.time()

with open('input.txt') as inputFile:  
   for line in inputFile:
        input = line.split(', ')

#Test inputs
#input = ["R2", "L3"]
#input = ["R2", "R2", "R2"]
#input = ["R5", "L5", "R5", "R3"]
result = 0

#0 - North
#1 - East
#2 - South
#3 - West
currDir = 0
row = 0
col = 0

for step in input:
    #First decide which way to go
    if step[0] == "L":
        if currDir == 0:
            currDir = 3
        else:
            currDir -= 1
    elif step[0] == "R":
        if currDir == 3:
            currDir = 0 
        else:
            currDir += 1
    else:
        print("Wrong move")
    
    #move proper amount of steps
    if currDir==0:
        row += int(step[1:])
    elif currDir==2:
        row -= int(step[1:])
    elif currDir==1:
        col += int(step[1:])
    elif currDir==3:
        col -= int(step[1:])
        
print(row,  col)
print("Result: ",  abs(row)+abs(col))

end = time.time()
print("Took: ",  end-start)

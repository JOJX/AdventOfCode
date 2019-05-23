import time
start = time.time()

with open('input.txt') as inputFile:  
   for line in inputFile:
        input = line.split(', ')

#input = ["R8", "R4", "R4", "R8"]
result = -1

#0 - North
#1 - East
#2 - South
#3 - West
currDir = 0
row = 0
col = 0

locations = []
#Add starting position
locations.append((0, 0)) 

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
    
    #move proper amount of steps and save every location between
    if currDir==0:
        #To register every position
        for i in range(row+1, row+int(step[1:])+1):
            #check if position was already visited
            if (i, col) in locations:
                #print result coordinates
                print(i, col)
                #save distance from starting position
                result = abs(i)+abs(col)
                break
            else:
                #position not visited yet, add to the list
                locations.append((i, col))
        #Move cursor to the now position
        row += int(step[1:])
        
    elif currDir==2:
        for i in range(row-1,  row-int(step[1:])-1, -1):
            if (i, col) in locations:
                print(i, col)
                result = abs(i)+abs(col)
                break
            else:
                locations.append((i, col))
        row -= int(step[1:])
        
    elif currDir==1:
        for i in range(col+1, col+int(step[1:])+1):
            if (row, i) in locations:
                print(row, i)
                result = abs(row)+abs(i)
                break
            else:
                locations.append((row, i))
        col += int(step[1:])
        
    elif currDir==3:
        for i in range(col-1,  col-int(step[1:])-1, -1):
            if (row, i) in locations:
                print(row,  i)
                result = abs(row)+abs(i)
                break
            else:
                locations.append((row, i))
        col -= int(step[1:])
        
    #If result was found in previous step then stop
    if result != -1:
        break
    
print("Result: ", result )

end = time.time()
print("Took: ",  end-start)

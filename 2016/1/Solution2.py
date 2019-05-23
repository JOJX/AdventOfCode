with open('input.txt') as inputFile:  
   for line in inputFile:
        input = line.split(', ')

#input = ["R8", "R4", "R4", "R8"]
result = 0

#0 - North
#1 - East
#2 - South
#3 - West
currDir = 0
row = 0
col = 0
locations = []
locations.append((0, 0))

for step in input:
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
    
    if currDir==0:
        for i in range(row+1, row+int(step[1:])+1):
            if (i, col) in locations:
                print(i, col)
                break
            else:
                locations.append((i, col))
        row += int(step[1:])
    elif currDir==2:
        for i in range(row-1,  row-int(step[1:])-1, -1):
            if (i, col) in locations:
                print(i, col)
                break
            else:
                locations.append((i, col))
        row -= int(step[1:])
    elif currDir==1:
        for i in range(col+1, col+int(step[1:])+1):
            if (row, i) in locations:
                print(row, i)
                break
            else:
                locations.append((row, i))
        col += int(step[1:])
    elif currDir==3:
        for i in range(col-1,  col-int(step[1:])-1, -1):
            if (row, i) in locations:
                print(row,  i)
                break
            else:
                locations.append((row, i))
        col -= int(step[1:])

#print(row,  col)

with open('input.txt') as inputFile:  
   for line in inputFile:
        input = line.split(',')

from itertools import repeat

#input = ['nw', 'se', 'nw', 'se', 'se', 'se']
input[len(input)-1] = "se"

def solve(input):
    col = 0
    row = 0
    for m in input: 
        if m == "n":
            row += 1
        elif m == "ne":
            if abs(col)% 2:
                row += 1
            col += 1
        elif m == "nw":
            if abs(col) % 2:
                row += 1
            col -= 1
           
        elif m == "s":
            row -= 1
        elif m == "se":
            if not abs(col) % 2:
                row -= 1
            col += 1
            
        elif m == "sw":
            if not abs(col) % 2:
                row -= 1
            col -= 1
            
        else:
            print("WRONG MOVE")
    return (col,  row)
        
col, row = solve(input)

print("Position of the program: Column: ",  col,  " Row: ",  row)

def recreate(col,  row, prevCol=0, prevRow=0):
    #first go ne
    if col>prevCol and row > prevRow:
        pass
    #first go se
    elif col > prevCol and row < prevRow:
        resInput = list(repeat("se",abs(col) ))
    #first go nw
    elif col < prevCol and row > prevRow:
        resInput = list(repeat("nw",abs(col) ))
    #first go sw
    else:
        resInput = list(repeat("sw",abs(col) ))
    return resInput
    
resInput = recreate(col, row)
    
resCol,  resRow = solve(resInput)

print("Column: ",  resCol)
print("Row: ",  resRow)

result = abs(col)+(row-resRow)
print(result)

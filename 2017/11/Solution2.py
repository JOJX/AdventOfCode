with open('input.txt') as inputFile:  
   for line in inputFile:
        input = line.split(',')

from itertools import repeat

#input = ['nw', 'se', 'nw', 'se', 'se', 'se',  's']
input[len(input)-1] = "se"

def recreate(targetCol,  targetRow, prevCol=0, prevRow=0):
    #first go ne
    resInput= []
    if targetCol>prevCol and targetRow > prevRow:
        for i in range(0, min(abs(targetCol),  abs(targetRow))):
            resInput.append("ne")
    #first go se
    elif targetCol > prevCol and targetRow < prevRow:
        for i in range(0, min(abs(targetCol),  abs(targetRow))):
            resInput.append("se")
    #first go nw
    elif targetCol < prevCol and targetRow > prevRow:
        for i in range(0, min(abs(targetCol),  abs(targetRow))):
            resInput.append("nw")
    #first go sw
    else:
        for i in range(0, min(abs(targetCol),  abs(targetRow))):
            resInput.append("sw")
    
    result = 0
    row =0 
    col =0
    #see how far we get using only ne/se/nw/sw
    for m in resInput: 
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
            
    if col == targetCol:
        result = abs(col )+ abs(targetRow)-abs(row)
    elif row == targetRow:
        result = abs(row )+ abs(targetCol)-abs(col)
    return result
    
def solve(input):
    col = 0
    row = 0
    maxProx = 0
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
        prox = recreate(col, row)
        if prox > maxProx:
            maxProx= prox
            
    return (col,  row, maxProx)
        
col, row, prox = solve(input)

print("PROX: ", prox )
print("Position of the program: Column: ",  col,  " Row: ",  row)


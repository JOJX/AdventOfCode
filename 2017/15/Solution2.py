from itertools import repeat
import time

start = time.time()

#Result for that = 8108
#input = "flqrgnkx-"

input = "ljoxqyyw-"

def knotHash(input):
    lenghts = []
    for i in range(0, len(input)):
        lenghts.append(ord(input[i]))
    suffix = [17, 31, 73, 47, 23]
    for e in suffix:
        lenghts.append(e)

    string = list(range(0, 256))
    skipSize=0
    currPos=0 

    for r in range(0, 64):
        for lenght in lenghts:
            if lenght <= len(string):
                if currPos+lenght < len(string):
                    subset = string[currPos:((currPos+lenght)%len(string))]
                    subset.reverse()
                    string[currPos:(currPos+lenght)] = subset
                else:
                    for i in range(0, lenght):
                        subset.append(string[(currPos+i)%len(string)])
                    subset.reverse()
                    for i in range(0, lenght):
                        string[(currPos+i)%len(string)] = subset[i]
        
                currPos = (currPos + lenght + skipSize) % len(string)
                skipSize += 1
                subset.clear()
            else:
                continue

    #print("Sparse hash: ",  string)
    denseHash = list(repeat(0, 16))

    for i in range(0, 16):
        subhash = string[i*16:(i*16+16)]
        denseHash[i] = subhash[0]
        for j in range(1, 16):
            denseHash[i] ^= subhash[j]
        
    #print("Dense hash: ",  denseHash)
    result = list("")

    for h in denseHash:
        temp = list(hex(h))
        del temp[0] 
        del temp[0]
        if len(temp) == 1:
            temp.append(temp[0])
            temp[0] = '0'
        result+=temp
    #print("Solution: ",  "".join(result))
    return result
#END OF KNOT HASH

result = 0
disk = []
diskLine = str()
for i in range(0, 128):
    currInput = input + str(i)
    #print(currInput)
    hash = knotHash(currInput)
    for bit in hash:
        binRep = bin(int(bit,  16))
        binRep = binRep[2:]
        if len(binRep) < 4:
            zerosInFront = 4-len(binRep)
            for i in range(0, zerosInFront):
                binRep = '0'+ binRep    
        #print(binRep)
        diskLine = diskLine + binRep   
    disk.append(diskLine)
    diskLine = ''
    
print()
print(disk)

#vertex para koordynatów (x,y)
def neighbours( vertex ):
    result = []
    x, y = vertex
    if x > 0:
        result.append((x-1,  y))
    if x < 127:
        result.append((x+1,  y))
    if y > 0:
        result.append((x,  y-1))
    if y < 127:
        result.append((x,  y+1))
    return result
    
regions = []
visited =  set()

#start - para koordynatów
def dfs( start ):
    stos = set()
    stos.add(start)
    members = []
    members.append(start)
    while len(stos):
        vertex = stos.pop()
        if vertex not in visited:
            visited.add(vertex)
            for dest in neighbours(vertex):
                x, y = dest
                #print(disk[x][y])
                if (disk[x][y] == '1') and ( (x, y) not in visited):
                    stos.add(dest)
                    members.append(dest)
    return members
    
k = 0
for i in range(0, 128):
    for j in range(0, 128):
        if disk[i][j] == '1' and (i, j) not in regions and (i, j) not in visited:
            regions.append(dfs((i, j)))
            

print(len(regions))
end = time.time()
print("Took: ",  end - start)


#from itertools import repeat

source = []
destinations = []

with open('input.txt') as inputFile:  
   for line in inputFile:
        line = line.replace(',', '')
        input = line.split()
        source.append(input[0])
        destinations.append(input[2:])
        
resultList = set()
resultList.add(0)

def dfs( start ):
    visited =  set()
    stos = set()
    stos.add(start)

    while len(stos):
        vertex = stos.pop()
        if vertex not in visited:
            visited.add(vertex)
            for dest in destinations[vertex]:
                stos.add(int(dest))
                resultList.add(int(dest))

dfs(0)
print(resultList)
print(len(resultList))

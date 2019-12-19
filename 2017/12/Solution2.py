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

visited =  set()

def dfs( start ):
    stos = set()
    stos.add(start)

    while len(stos):
        vertex = stos.pop()
        if vertex not in visited:
            visited.add(vertex)
            for dest in destinations[vertex]:
                stos.add(int(dest))
                resultList.add(int(dest))

result = 0

for program in source:
    if int(program) not in visited:
        dfs(int(program))
        result+=1
        
print(result)




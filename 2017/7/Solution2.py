
data = {}
dataWithChildren = {}
sums = {}

def dfs( name ):
    stos = []
    stos.append(name)
#    data[name][2] = True   #Mark as visited
    sum =0
    while len(stos):
        n = stos.pop()
        for w in data[n][1]:
            stos.append(w)
            sum += int(data[w][0])
        sum += int(data[n][0])
        sums[n] = sum
        sum =0
        
#Prepare input as a list of custom class objects
with open('testInput.txt') as inputFile:  
   for line in inputFile:
        parameters=line.split()
        parameters[1] = parameters[1].replace('(', '')
        parameters[1] = parameters[1].replace(')', '')
        children = []

        if len(parameters)>2:
            for x in range(3, len(parameters), 1):
                parameters[x] = parameters[x].replace(',', '')
                children.append(parameters[x])
            dataWithChildren[parameters[0]]=(parameters[1], children, False)
        data[parameters[0]]=[parameters[1], children, 0]
        
result = ''
# data = dict{name: (weight, listOfChildren)}
# Find the root
for name in dataWithChildren:
    flag = False
    for k,v   in dataWithChildren.items():
        if name in v[1]:
            flag = False
            break
        else:
            flag = True
    if flag:
        result = name
        
print("Root: ",  result)
print("Number of children: ",  data[result][1])

dfs(result)
#for c in data[result][1]:
#    print(c,  sums[c])
print(sums)

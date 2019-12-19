
class ProgramObject():
    def __init__(self, name,  weight, children=['']):
        self.name = name #String
        self.weight = weight #int
        self.children = children #list of strings
    
    def __str__(self):
        return "%s -> %s" % (self.name,  self.children)
    def hasChildren(self):
        return not self.children.empty()
    def find(self,  name):
        return name in self.children
input = []
inputWithChildren = []

#Prepare input as a list of custom class objects
with open('input.txt') as inputFile:  
   for line in inputFile:
        parameters=line.split()
        parameters[1] = parameters[1].replace('(', '')
        parameters[1] = parameters[1].replace(')', '')
        children = []
        
        if len(parameters)>2:
            for x in range(3, len(parameters), 1):
                parameters[x] = parameters[x].replace(',', '')
                children.append(parameters[x])
            inputWithChildren.append(ProgramObject(parameters[0], parameters[1], children))
        input.append(ProgramObject(parameters[0], parameters[1], children))
        
for program in inputWithChildren:
    name = program.name
    flag = False
    for prog in inputWithChildren:
        if prog.find(name):
            flag = False
            break
        else:
            flag = True
    if flag:
        result = program

print("Solution: ",  result.name)

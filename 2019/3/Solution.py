lineA = []
lineB = []

with open('input.txt') as inputFile:
    lines = inputFile.readlines()
    for el in lines[0].split(','):
        lineA.append(el)
    for el in lines[1].split(','):
        lineB.append(el)

visitedPointsA = []
visitedPointsB = []
crossPoints = []

x = 0
y = 0
distance = 999999999999999

def markPoints(lineCommands, visitedPoints,x,y):
    for step in lineCommands:
        steps = int(step[1:])+1
        if step[0] == 'U':
            for i in range(y, y+steps,1):
                visitedPoints.append((x,i))
            y=y+steps-1
        elif step[0] == 'D':
            for i in range(y, y-steps,-1):
                visitedPoints.append((x,i))
            y=y-steps+1
        elif step[0] == 'R':
            for i in range(x, x+steps):
                visitedPoints.append((i,y))
            x=x+steps-1
        elif step[0] == 'L':
            for i in range(x, x-steps,-1):
                visitedPoints.append((i,y))
            x=x-steps+1

def countDistance(point):
    return abs(point[0]) + abs(point[1])

def lookForCrossPoint(mapA, mapB, distance):
    for point in mapA:
        if point in mapB and point != (0,0):
            #crossPoints.append(point)
            currDist = countDistance(point)
            if currDist < distance and currDist != 0:
                distance = currDist
    return distance



markPoints(lineA, visitedPointsA,x,y)
x=0
y=0
markPoints(lineB, visitedPointsB,x,y)
distance = lookForCrossPoint(visitedPointsA, visitedPointsB, distance)

print(distance)
#print("Final result: ", input)

planets = []
orbiters = []

with open('input.txt') as inFile:
   for line in inFile:
        line = line.rstrip()
        planet, orbiter = line.split(")")
        planets.append(planet)
        orbiters.append(orbiter)

class Planet:
    def __init__(self, name, orbitsAround):
        self.name = name
        self.orbitsAround = orbitsAround
        self.ownOrbiters = []

    def addOrbiter(self, orbiter):
        self.ownOrbiters.append(orbiter)

    def getPredecesor(self):
        if self.orbitsAround != '':
            return self.orbitsAround
        else:
            return False

planetsDict = {}

for i in range(0, len(orbiters)):
    if i == 0:
        p = Planet(planets[i], '')
        planetsDict[planets[i]]= p

    p=Planet(orbiters[i], planets[i])

    planetsDict[orbiters[i]]= p

    if planets[i] in planetsDict:
        planetsDict[planets[i]].addOrbiter(orbiters[i])
    else:
        p = Planet(planets[i], '')
        planetsDict[planets[i]]= p

result = 0

YOU = planetsDict['YOU']
SAN = planetsDict['SAN']
commonPlanet = planetsDict['COM']

youPred = []
sanPred = []
planet = YOU

while planet.getPredecesor():
    youPred.append(planetsDict[planet.getPredecesor()])
    planet = planetsDict[planet.getPredecesor()]

planet = SAN

while planet.getPredecesor():
    pre = planetsDict[planet.getPredecesor()]
    sanPred.append(pre)
    if pre in youPred:
        result += len(sanPred) -1
        commonPlanet = pre
        break
    planet = pre

for i in range(0,len(youPred)):
    if youPred[i] == commonPlanet:
        result += i

print("RESULT: ", result)
import time

start = time.time()

startA =  722
startB = 354

factorA = 16807
factorB = 48271

divider = 2147483647

def generatorA( source ):
    result = (source*factorA)%divider
    return result
    
def generatorB( source ):
    result = (source*factorB)%divider
    return result
    
result = 0
for i in range(0,  40000000):
    startA = generatorA(startA)
    startB = generatorB(startB)
    a = startA & 0x0000FFFF
    b = startB & 0x0000FFFF
    if a==b:
        result+=1

end = time.time()
print("Took: ",  end-start)
print(result)

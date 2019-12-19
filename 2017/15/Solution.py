import time

with open('input.txt') as inputFile:  
   for line in inputFile:
        input = line.split(',')

#input = ['s3', 'x3/4',  'pe/b']
#programs = ['a', 'b',  'c',  'd',  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

programs = "abcdefghijklmnop"

start = time.time()

for move in input:
    if move[0] == 's':
        #print("SPIN")
        programs = programs[len(programs)- int(move[1:] ) : len(programs)] + programs[0 : len(programs)- int(move[1:])]

    elif move[0] == 'x':
        #print("EXCHANGE")
        A = int(move[1:move.find('/')])
        B = int(move[move.find('/')+1:])
        progs = list(programs)
        progs[A],  progs[B] = progs[B],  progs[A] 
        programs  = ''.join(progs)
        
    elif move[0] == 'p':
        #print("PARTNER")
        A = move[1]
        B = move[3]
        A = programs.find(A)
        B = programs.find(B)
        progs = list(programs)
        progs[A],  progs[B] = progs[B],  progs[A] 
        programs  = ''.join(progs)  
        
    else:
        print("Wrong move")
    
print("Final sequence: ",  programs)
end = time.time()
print("Took: ",  end-start)
#print(result)

from itertools import repeat

#input = "14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244"
#input = "AoC 2017" #33efeb34ea91902bb2f59c9920caa6cd
#input = "1,2,3" #3efbe78a8d82f29979031a4aa0b16a9d
#input = "1,2,4" #63960835bcdc130f0b66d7ff4f6a5a8e

input = "flqrgnkx-0"

lenghts = []
for i in range(0, len(input)):
    lenghts.append(ord(input[i]))
suffix = [17, 31, 73, 47, 23]
for e in suffix:
    lenghts.append(e)
print(lenghts)

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

print("Sparse hash: ",  string)
denseHash = list(repeat(0, 16))

for i in range(0, 16):
    subhash = string[i*16:(i*16+16)]
    denseHash[i] = subhash[0]
    for j in range(1, 16):
        denseHash[i] ^= subhash[j]
        
print("Dense hash: ",  denseHash)
result = list("")

for h in denseHash:
    temp = list(hex(h))
    del temp[0] 
    del temp[0]
    if len(temp) == 1:
        temp.append(temp[0])
        temp[0] = '0'
    result+=temp
print("Solution: ",  "".join(result))

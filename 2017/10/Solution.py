lenghts = [14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244]

#TEST what is the result of multiplying the first two numbers in the list? 3x4=12
#lenghts = [3, 4, 1, 5]

string = list(range(0, 256))
skipSize=0
currPos=0 

for lenght in lenghts:
    if lenght <= len(string):
        if currPos+lenght <= len(string):
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

result = string[0]*string[1] 
print(string)
print("Solution: ",  result)

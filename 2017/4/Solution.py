inputFile = open('input.txt')
input = inputFile.readlines()

#input = ["aa bb cc dd ee","aa bb cc dd aa", "aa bb cc dd aaa" ]
listOfWords= []
result = 0

for line in input:
    listOfWords = line.split()
    for word in listOfWords:
        if( listOfWords.count(word) > 1 ):
            flag=False
            break
            
        else:
            flag = True
    if(flag):
        result += 1
        
print(result)

input2 = ["abcde fghij","abcde xyz ecdab", "a ab abc abd abf abj", "iiii oiii ooii oooi oooo", "oiii ioii iioi iiio" ]

inputFile = open('input.txt')
input = inputFile.readlines()

input2 = ["abcde fghij","abcde xyz ecdab", "a ab abc abd abf abj", "iiii oiii ooii oooi oooo", "oiii ioii iioi iiio" ]
listOfWords= []
result = 0

for line in input:
    listOfWords = line.split()
    for index, word in enumerate(listOfWords):
        listOfWords[index] = ''.join(sorted(word))
    print(listOfWords)

    for word in listOfWords:
        if( listOfWords.count(word) > 1 ):
            flag=False
            break
        else:
            flag = True
    if(flag):
        result += 1
        
print("Solution for puzzle 4, part 2: ")
print(result)


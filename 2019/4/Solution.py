lowerBound = 271973
upperBound = 785961
correctPasswords = []

#Digits never decrease
def checkForOrder(number):
    return number[0] <= number[1] and number[1] <= number[2] and number[2] <= number[3] and number[3] <= number[4] and number[4] <= number[5]
    
#Must have at least one pair of same adjacent digits
def checkForPair(number):
    return number[0] == number[1] or number[1] == number[2] or number[2] == number[3] or number[3] == number[4] or number[4] == number[5]

for i in range(lowerBound, upperBound, 1):
    if checkForPair(str(i)) and checkForOrder(str(i)):
        correctPasswords.append(i)

print(len(correctPasswords))
#print("Final result: ", intCode)

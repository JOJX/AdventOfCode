
input = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3,	14, 5, 12, 3]
#Test input below - should return 5
#input = [0, 2, 7, 0] 

result = 0
combinations = list()

while input not in combinations:
    combinations.append(input[:])
    blocks = max(input)
    bank = input.index(blocks)
    input[bank]=0
    for i in range(1, blocks+1, 1):
        input[(bank+i)%len(input)] += 1
    result += 1

print("Solution: ",  result)

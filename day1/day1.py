inputFile = open("day1/day1.txt", "r")
inputString = inputFile.read()
inputFile.close()
result = 0

for i in range(0, len(inputString)):
    c = inputString[i]

    if i + 1 < len(inputString):
        nextC = inputString[i + 1]
    else:
        nextC = inputString[0]

    if c == nextC:
        result = result + int(c)

print(result)
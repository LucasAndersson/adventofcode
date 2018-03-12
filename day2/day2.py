inputFile = open("day2.txt", "r")
inputString = inputFile.read()
inputFile.close()

rows = inputString.splitlines()
checksum = 0

for r in rows:
    r = r.split()
    r = list(map(int, r))
    sortedR = sorted(r)
    mi = int(sortedR[0])
    ma = int(sortedR[len(r) - 1])
    checksum += ma - mi

print(checksum)

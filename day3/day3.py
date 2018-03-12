class Point:
    x, y = -1, -1

    def __init__(self, x, y):
        self.x = x
        self.y = y


w, h = 1000, 1000
matrix = [[0 for x in range(w)] for y in range(h)]
centerX = int((w) / 2)
centerY = int((h) / 2)

matrix[centerX][centerY] = 1
lastX, lastY = centerX, centerY
matrix[lastX][lastY + 1] = matrix[lastX][lastY] + 1
lastY = lastY + 1


def generateSpiral(lastX, lastY):
    while True:
        # go right until node below is 0
        while matrix[lastX - 1][lastY] != 0:
            if (lastY + 1) < h:
                matrix[lastX][lastY + 1] = matrix[lastX][lastY] + 1
                lastY = lastY + 1
            else:
                return
        # go up until node to left is 0
        while matrix[lastX][lastY - 1] != 0:
            matrix[lastX - 1][lastY] = matrix[lastX][lastY] + 1
            lastX = lastX - 1

        # go left until node below is 0
        while matrix[lastX + 1][lastY] != 0:
            matrix[lastX][lastY - 1] = matrix[lastX][lastY] + 1
            lastY = lastY - 1

        # go down until node to right is 0
        while matrix[lastX][lastY + 1] != 0:
            matrix[lastX + 1][lastY] = matrix[lastX][lastY] + 1
            lastX = lastX + 1


generateSpiral(lastX, lastY)

for m in matrix:
    print(m)

def doStuff(i):
    for x in range(w):
        for y in range(h):
            if matrix[x][y] == i:
                return Point(y, x)

res = doStuff(8)
print("centerX: " + str(centerX) + ", centerY: " + str(centerY))
print("x: " + str(res.x) + ", y: " + str(res.y))

manhattan = (centerX - res.x) + (centerY - res.y)
manhatan2 = (res.x - centerX) + (res.y - centerY)
print("manhattan: " + str(manhattan))
print("manhattan2: " + str(manhatan2))


import sys
import re

file = open("./day15/input.txt", "r")
content = file.read()
file.close()

map = content.split("\n")
yMax = len(map)
xMax = len(map[0])

wallList = []
start = ()
end = ()

# fill positions
for yInd in range(yMax):
    for xInd in range(xMax):
        char = map[yInd][xInd]
        if(char == "#"):
            wallList.append((yInd, xInd))
        if(char == "S"):
            start = (yInd, xInd)
        if(char == "E"):
            end = (yInd, xInd)


def checkNext(pos, num):
    global nines
    score = 0
    dir = (-1, 0)
    next = num + 1
    for i in range(4):
        nextPos = (pos[0] + dir[0], pos[1] + dir[1])
        if(-1 < nextPos[0] and nextPos[0] < yMax and -1 < nextPos[1] and nextPos[1] < xMax):
            if(map[nextPos[0]][nextPos[1]] == str(next)):
                if(next == 9):
                    if(nextPos not in nines):
                        nines.append(nextPos)
                    score += 1
                else:
                    score += checkNext(nextPos, next)
        dir = (dir[1], -dir[0])
    return score
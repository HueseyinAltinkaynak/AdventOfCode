import sys
import re

file = open("./day10/input.txt", "r")
content = file.read()
file.close()

map = content.split("\n")
yMax = len(map)
xMax = len(map[0])

nines = []

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

total1 = 0
total2 = 0

for yInd in range(yMax):
    for xInd in range(xMax):
        if(map[yInd][xInd] == "0"):
            nines = []
            total2 += checkNext((yInd, xInd), 0)
            total1 += len(nines)

print("Part 1: ", total1)
print("Part 2: ", total2)

#print(checkNext((0,2), 0))
import sys
import re

file = open("./day12/input.txt", "r")
content = file.read()
file.close()

map = content.split("\n")
yMax = len(map)
xMax = len(map[0])


def getRegion(pos):
    region = [pos]
    digitsChecked = []
    digitsNotChecked = [pos]
    char = map[pos[0]][pos[1]]
    dir = (-1, 0)
    totalPerim = 0
    totalSides = 0
    curPos = pos
    while(len(digitsNotChecked) > 0):
        for i in range(4):
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if(-1 < nextPos[0] and nextPos[0] < yMax and -1 < nextPos[1] and nextPos[1] < xMax):
                nextChar = map[nextPos[0]][nextPos[1]]
                if(nextChar == char):
                    if(nextPos not in region):
                        region.append(nextPos)
                        digitsNotChecked.append(nextPos)
                    else:
                        if(nextPos not in digitsChecked):
                            if(nextPos not in digitsNotChecked):
                                digitsNotChecked.append(nextPos)

            dir = (dir[1], -dir[0])

        totalPerim += calcPerim(curPos)
        totalSides += calcCorner(curPos)
        # print("checked digit:", curPos, corner)
        digitsChecked.append(curPos)
        digitsNotChecked.remove(curPos)
        try:
            curPos = digitsNotChecked[0]
        except Exception:
            curPos = None
    region.sort()
    return (char, region, len(region), totalPerim, totalSides)

def calcPerim(pos):
    dir = (-1, 0)
    char = map[pos[0]][pos[1]]
    perim = 0
    for i in range(4):
        nextPos = (pos[0] + dir[0], pos[1] + dir[1])
        if(-1 < nextPos[0] and nextPos[0] < yMax and -1 < nextPos[1] and nextPos[1] < xMax):
            nextChar = map[nextPos[0]][nextPos[1]]
            if(nextChar != char):
                perim += 1
        else:
            perim += 1

        dir = (dir[1], -dir[0])

    return perim

def calcCorner(pos):
    dir = (-1, 0)
    char = map[pos[0]][pos[1]]
    corner = 0
    fence = 0
    prevFence = 0
    firstFence = 0
    for i in range(4):
        prevFence = fence
        if(i == 1):
            firstFence = fence
        nextPos = (pos[0] + dir[0], pos[1] + dir[1])
        if(-1 < nextPos[0] and nextPos[0] < yMax and -1 < nextPos[1] and nextPos[1] < xMax):
            nextChar = map[nextPos[0]][nextPos[1]]
            if(nextChar != char):
                fence = 1
            else:
                fence = 0
        else:
            fence = 1

        dir = (dir[1], -dir[0])

        if(i > 0):
            if(prevFence == fence):
                if(fence == 0):
                    oppCorner = (pos[0]-dir[0]-dir[1], pos[1]-dir[1]+dir[0])
                    oppChar = ""
                    try:
                        oppChar = map[oppCorner[0]][oppCorner[1]]
                    except Exception:
                        print("first")
                    if(oppChar != char):
                        corner += 1
                else:
                    corner += 1

    dir = (dir[1], -dir[0])

    if(firstFence == fence):
        if(fence == 0):
            oppCorner = (pos[0]-dir[0]-dir[1], pos[1]-dir[1]+dir[0])
            oppChar = ""
            try:
                oppChar = map[oppCorner[0]][oppCorner[1]]
            except Exception:
                        print("second")
            if(oppChar != char):
                corner += 1
        else:
            corner += 1

    return corner


regions = []

checked = []

yInd = 0
xInd = 0

while(yInd < yMax):
    if(xInd >= xMax):
        xInd = 0
        yInd += 1
        continue
    if((yInd, xInd) in checked):
        xInd += 1
        continue

    checked.append((yInd, xInd))

    reg = getRegion((yInd, xInd))
    reg = reg[:]

    if(reg not in regions):
        regions.append(reg)
    xInd += 1

total1 = 0
total2 = 0

for region in regions:
    total1 += region[2] * region[3]
    total2 += region[2] * region[4]

print("Part 1: ", total1)
print("Part 2: ", total2)

# for region in regions:
#     print(region)

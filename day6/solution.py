import sys
import re

def check_loop(altMap):
    posY = startY
    posX = startX

    dir = (-1, 0)

    bumped = []

    loop = False

    while (-1 < posY + dir[0] and posY + dir[0] < maxY and -1 < posX + dir[1] and posX + dir[1] < maxX):
        if (altMap[posY+dir[0]][posX+dir[1]] == "#"):
            if((posY+dir[0], posX+dir[1], dir) in bumped):
                loop = True
                break
            else:
                bumped.append((posY+dir[0], posX+dir[1], dir))
            dir = (dir[1], -dir[0])

        else:
            posY += dir[0]
            posX += dir[1]

    return loop

file = open("./day6/input.txt", "r")
content = file.read()
file.close()

map = content.split("\n")

single = content.replace("\n", "")

maxY = len(map)
maxX = len(map[0])
pos = re.search("\^", single)
startY = int(pos.start()/maxX)
startX = pos.start() - startY * maxX

posY = startY
posX = startX

visited = [(posY, posX)]

dir = (-1, 0)

while (-1 < posY + dir[0] and posY + dir[0] < maxY and -1 < posX + dir[1] and posX + dir[1] < maxX):
    if (map[posY+dir[0]][posX+dir[1]] == "#"):
        dir = (dir[1], -dir[0])
    else:
        posY += dir[0]
        posX += dir[1]
        if(not ((posY, posX) in visited)):
            visited.append((posY, posX))

possibilitys = visited.copy()

possibilitys.pop(0)

count = 0

for v in possibilitys:
    newMap = map.copy()
    newMap[v[0]] = newMap[v[0]][:v[1]] + "#" + newMap[v[0]][v[1]+1:]
    
    if(check_loop(newMap)):
        count += 1

print(len(visited))
print(count)
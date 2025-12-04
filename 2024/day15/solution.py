import sys
import re

file = open("./day15/input.txt", "r")
content = file.read()
file.close()

split = content.split("\n\n")
map = split[0].split("\n")
moves =split[1].replace("\n", "")

wallList = []
wallList2 = []
boxList = []
boxList2 = []
robot = (0, 0)
robot2 = (0, 0)

# fill Lists
for yInd in range(len(map)):
    for xInd in range(len(map[0])):
        if (map[yInd][xInd] == '#'):
            wallList.append((yInd, xInd))
            wallList2.append((yInd, xInd * 2))
            wallList2.append((yInd, xInd * 2 + 1))
        elif (map[yInd][xInd] == 'O'):
            boxList.append((yInd, xInd))
            boxList2.append(((yInd, xInd * 2), (yInd, xInd * 2 + 1)))
        elif (map[yInd][xInd] == '@'):
            robot = (yInd, xInd)
            robot2 = (yInd, xInd * 2)

def getDir(char):
    if(char == "^"):
        return (-1, 0)
    elif(char == ">"):
        return (0, 1)
    elif(char == "v"):
        return (1, 0)
    elif(char == "<"):
        return (0, -1)
    else:
        return (0, 0)
    
def move(pos, dir, isRobot):
    global robot
    global boxList
    nextPos = (pos[0] + dir[0], pos[1] + dir[1])
    if(nextPos in wallList):
        return False
    elif(nextPos in boxList):
        movedNext = move(nextPos, dir, False)
        if(movedNext):
            if(isRobot):
                robot = nextPos
            else:
                boxList.remove(pos)
                boxList.append(nextPos)
            return True
        else:
            return False
    else:
        if(isRobot):
            robot = nextPos
        else:
            boxList.remove(pos)
            boxList.append(nextPos)
        return True
    
def moveRobot(pos, dir):
    global robot2

    nextPos = (pos[0] + dir[0], pos[1] + dir[1])
    nextBox = checkBox(nextPos)

    if(nextPos in wallList2):
        return False
    elif(nextBox != None):
        if(movable(nextBox, dir)):
            robot2 = nextPos
            moveBox(nextBox, dir)
        return movable(nextBox, dir)
    else:
        robot2 = nextPos
        return True
    
def moveBox(pos, dir):
    global boxList2
    nextPos = []

    if(dir[0] == 0):
        nextPos.append((pos[0][0], pos[int((dir[1]+1)/2)][1] + dir[1]))
    else:
        nextPos.append((pos[0][0] + dir[0], pos[0][1]))
        nextPos.append((pos[1][0] + dir[0], pos[1][1]))

    for Pos in nextPos:
        nextBox = checkBox(Pos)
        if(nextBox != None):
            moveBox(nextBox, dir)
    
    boxList2.remove(pos)
    boxList2.append(((pos[0][0] + dir[0], pos[0][1] + dir[1]), (pos[1][0] + dir[0], pos[1][1] + dir[1])))

def movable(pos, dir):
    nextPos = []
    valid = True

    if(dir[0] == 0):
        nextPos.append((pos[0][0], pos[int((dir[1]+1)/2)][1] + dir[1]))
    else:
        nextPos.append((pos[0][0] + dir[0], pos[0][1]))
        nextPos.append((pos[1][0] + dir[0], pos[1][1]))

    for Pos in nextPos:
        nextBox = checkBox(Pos)
        if(Pos in wallList2):
            return False
        elif(nextBox != None):
            valid = movable(nextBox, dir)
            if(not valid):
                return False
    
    return valid
  
def checkBox(pos):
    box1 = ((pos[0], pos[1] - 1), (pos[0], pos[1]))
    box2 = ((pos[0], pos[1]), (pos[0], pos[1] + 1))
    if(box1 in boxList2):
        return box1
    elif(box2 in boxList2):
        return box2
    else:
        return None  
    
def updateMap(map):
    for yInd in range(len(map)):
        for xInd in range(len(map[0])):
            mapPos = (yInd, xInd)
            if (mapPos in wallList):
                continue
            elif (mapPos in boxList):
                map[yInd] = map[yInd][:xInd] + "O" + map[yInd][xInd+1:]
            elif (mapPos == robot):
                map[yInd] = map[yInd][:xInd] + "@" + map[yInd][xInd+1:]
            else:
                map[yInd] = map[yInd][:xInd] + "." + map[yInd][xInd+1:]
    return map  
    
def printMap(map):
    for line in map:
        print(line)


# move robot
for char in moves:
    dir = getDir(char)
    move(robot, dir, True)


total1 = 0

for box in boxList:
    total1 += 100 * box[0] + box[1]

print("Part 1: ", total1)



# move robot 2
for char in moves:
    dir = getDir(char)
    moveRobot(robot2, dir)


total2 = 0

for wideBox in boxList2:
    box = wideBox[0]
    total2 += 100 * box[0] + box[1]

print("Part 2: ", total2)
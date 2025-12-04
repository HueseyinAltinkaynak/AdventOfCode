import sys
import re

file = open("./day14/input.txt", "r")
content = file.read()
file.close()

robotsInput = content.split("\n")

# robots = {}
# robotsfinished = []
# robotsTree = {}

def saveRobots(width, height, seconds):
    index = 0
    robots = {}
    robotsfinished = []
    robotsTree = {}

    for robot in robotsInput:
        split = robot.split("=")
        splitpos = split[1].split(",")
        pos = (int(splitpos[0]), int(splitpos[1].replace(" v", "")))
        splitvelo = split[2].split(",")
        velo = (int(splitvelo[0]), int(splitvelo[1]))
        robots[index] = (pos, velo)
        finalX = (pos[0] + seconds * velo[0]) % width
        finalY = (pos[1] + seconds * velo[1]) % height
        robotsfinished.append((finalX, finalY))
        if(robotsTree.get((finalX, finalY)) == None):
            robotsTree[(finalX, finalY)] = 1
        else:
            robotsTree[(finalX, finalY)] += 1
        index += 1

    return (robots, robotsfinished, robotsTree)

def drawPicture(Tree, width, height):
    picture = ""
    for y in range(height):
        for x in range(width):
            if(Tree.get((x,y)) == None):
                picture += "."
            else:
                picture += str(Tree.get((x,y)))
        if(y < height-1):
            picture += "\n"

    return picture

def checkSymmetry(picture):
    lines = picture.split("\n")
    valid = True
    mid = int((len(lines[0])-1)/2)
    for line in lines:
        for i in range(mid):
            if(line[i] != line[mid*2-i]):
                valid = False
                break
        if(not valid):
            break
    return valid

# width = 101
# height = 103
# seconds = 100

# q1 = 0
# q2 = 0
# q3 = 0
# q4 = 0

# robots, robotsfinished, robotsTree = saveRobots(width, height, seconds)

# for robot in robotsfinished:
#     if(robot[0] < (width-1)/2):
#         if(robot[1] < (height-1)/2):
#             q1 += 1
#         elif(robot[1] > (height-1)/2):
#             q2 += 1
#     elif (robot[0] > (width-1)/2):
#         if(robot[1] < (height-1)/2):
#             q3 += 1
#         elif(robot[1] > (height-1)/2):
#             q4 += 1
# print("Part 1: ", q1 * q2 * q3 * q4)

width = 101
height = 103

i = 0

end = ""

while(end == ""):
    robots, robotsfinished, robotsTree = saveRobots(width, height, i)

    picture = drawPicture(robotsTree, width, height)
    

    if(checkSymmetry(picture) or i > 1000):
        print("Seconds: ", i)
        print(picture)
        break
    i += 1
    #end = input()


# print("Seconds: ", seconds)
# print(picture)
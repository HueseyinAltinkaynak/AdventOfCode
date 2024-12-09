import sys
import re

file = open("./day7/testinput.txt", "r")
content = file.read()
file.close()

def changeMode(m):
    if (m == "+"):
        return "*"
    else:
        return "+"

def check(line):
    s = line.split(": ")
    goal = int(s[0])
    steps = s[1].split(" ")
    start = int(steps[0])
    steps.pop(0)
    valid = False

    print("Goal: ", goal)

    indexMax = pow(2, len(steps))
    level = 0
    levelMode = {}

    index = 0

    total = start

    while(index < indexMax):
        if (levelMode.get(level) == None):
            levelMode[level] = "+"
            total += steps[level]

            if (level == 4):
                if (goal == total):
                    valid = True
                    break
                index += 1
            else:
                level += 1

        elif (levelMode.get(level) == "+"):
            levelMode[level] = "*"
            total *= steps[level]

            if (level == 4):
                if (goal == total):
                    valid = True
                    break
                index += 1
                level -= 1
                total /= steps[level]
            else:
                level += 1
        else:
            levelMode[level] = "+"
            total /= steps[level]

            

            if (level == 4):
                index += 1
                if (goal == total):
                    valid = True
                    break
                else:
                    level -= 1
            else:
                level += 1



        


    # for i in range(levels + 1):
    #     total = start
    #     print("------------------")
    #     print("Level: ", i)
    #     print("Start: ", total)
    #     for j in range(len(steps)):

    #         val = int(steps[j])
    #         if ((i - pow(2, len(steps) - j) ) % 2 == 1):         ((i - (i % 2)) / 2) % 2
    #             total *= val
    #         else:
    #             total += val
    #         print("Step: ", j, " new Total", total)

    #     if (total == goal):
    #         valid = True
    #         break
        
        
    if (valid):
        return goal
    else:
        return 0



lines = content.split("\n")

line = lines[1]



# print("Line: ", line)
# print("Check: ", check(line))

# total1 = 0

# for line in lines:
#     total1 += check(line)

# print("Part 1: ", total1)

#check(line)
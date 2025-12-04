import sys
import re

file = open("./day9/input.txt", "r")
content = file.read()
file.close()

controlList = []

finalindex = 0
posID = 0
negID = int((len(content)-1)/2)
negRemain = int(content[negID * 2])

total1 = 0

while(posID != negID):
    posVal = int(content[posID * 2])
    for i in range(posVal):
        total1 += finalindex * posID
        finalindex += 1
        controlList.append(posID)
    posID += 1
    for i in range(int(content[posID * 2 - 1])):
        if(negRemain == 0):
            negID -= 1
            negRemain = int(content[negID * 2])
        total1 += finalindex * negID
        finalindex += 1
        negRemain -= 1
        controlList.append(negID)

for i in range(negRemain):
    total1 += finalindex * negID
    finalindex += 1
    controlList.append(negID)


print("Part 1: ", total1)
#print(controlList)


usedSpace = []
controlList = []

finalindex = 0
posID = 0
negID = int((len(content)-1)/2)
negRemain = int(content[negID * 2])

total2 = 0

breakIndex = 0
while(posID != negID):
    posVal = int(content[posID * 2])
    if(posID in usedSpace):
        for i in range(posVal):
            controlList.append(".")
    else:
        for i in range(posVal):
            total2 += finalindex * posID
            finalindex += 1
            controlList.append(posID)
    posID += 1
    blank = int(content[posID * 2 - 1])
    while (blank > 0 and negID >= posID):
        if(negID in usedSpace):
            negID -= 1
            continue
        negSpace = int(content[negID * 2])
        if(negSpace > blank):
            negID -= 1
            continue
        else:
            blank -= negSpace
            usedSpace.append(negID)
            for i in range(negSpace):
                total2 += finalindex * negID
                finalindex += 1
                controlList.append(negID)
    finalindex += blank
    for i in range(blank):
        controlList.append(".")
    negID = int((len(content)-1)/2)
    

for i in range(int(content[posID * 2])):
    total2 += finalindex * posID
    finalindex += 1

# print("Part 2: ", total2) # irgendwie falsch

total3 = 0
for i in range(len(controlList)):
    if(controlList[i] == "."):
        continue
    else:
        total3 += i * int(controlList[i])
print("Part 2: ", total3)
#print(controlList)
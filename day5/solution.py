import sys
import re

file = open("./day5/input.txt", "r")
content = file.read()
file.close()

content = content.split("\n\n")

ordLines = content[0].split("\n")

updateLines = content[1].split("\n")

numDict = {}

for line in ordLines:
    pair = line.split("|")
    if(numDict.get(pair[0]) == None):
        numDict[pair[0]] = [0, [pair[1]]]
    else:
        numDict[pair[0]][1].append(pair[1])
    if(numDict.get(pair[1]) == None):
        numDict[pair[1]] = [numDict[pair[0]][0] + 1 , []]
    else:
        numDict[pair[1]][0] += 1
        for next in numDict[pair[1]][1]:
            numDict[next][0] += 1

# for line in numDict:
#     print(line, ": ",numDict[line])

total = 0
  
for line in updateLines:
    steps = line.split(",")
    valid = True
    for i in range(len(steps)-1):
        if(numDict[steps[i]][0] > numDict[steps[i+1]][0]):
            valid = False
            break
    if(valid):
        total += 1
        #total += int(steps[int(len(steps)/2)])

print(total)
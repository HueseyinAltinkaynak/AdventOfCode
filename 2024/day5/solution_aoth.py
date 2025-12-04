import sys
import re

content = sys.stdin.read()

content = content.split("\n\n")

ordLines = content[0].split("\n")

updateLines = content[1].split("\n")
updateLines.pop()



numDict = {}

for line in ordLines:
    pair = line.split("|")
    if(numDict.get(pair[0]) == None):
        numDict[pair[0]] = [pair[1]]
    else:
        numDict[pair[0]].append(pair[1])
    if(numDict.get(pair[1]) == None):
        numDict[pair[1]] = []

total = 0
total2 = 0
  
for line in updateLines:
    steps = line.split(",")
    valid = True
    for i in range(len(steps)-1):
        for j in range(i+1,len(steps)):
          if(numDict[steps[j]].__contains__(steps[i])):
              valid = False
              break
    if(valid):
        total += int(steps[int(len(steps)/2)])
    else:
        newList = []
        for num in steps:
            index = 0
            for i in range(len(newList)):
                if(numDict[newList[i]].__contains__(num)):
                    index += 1
                else:
                    break
            
            tempList = newList[index:]
            newList = newList[:index]
            newList.append(num)
            newList.extend(tempList)

        total2 += int(newList[int(len(newList)/2)])

print("Part 1: ", total)
print("Part 2: ", total2)
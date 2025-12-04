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
        numDict[pair[0]] = [pair[1]]
    else:
        numDict[pair[0]].append(pair[1])
    if(numDict.get(pair[1]) == None):
        numDict[pair[1]] = []

# for line in numDict:
#     print(line, ": ",numDict[line])

# print(len(numDict))

# testlist = [1, 4, 6, 3]

# print(testlist.__contains__(5))

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

# list = [4, 12, 8, 19, 48, 3, 3]
# l2 = [7, 91]
# newList = []

# for num in list:
#     index = 0
#     for i in range(len(newList)):
#         if(num > newList[i]):
#             index += 1
#         else:
#             break
    
#     tempList = newList[index:]
#     newList = newList[:index]
#     newList.append(num)
#     newList.extend(tempList)

# print(list)
# print(newList)

# #print(list[10:])
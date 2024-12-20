import sys
import re
from functools import cache

# file = open("./day11/input.txt", "r")
# content = file.read()
# file.close()

content = sys.stdin.read()

stones = content.split(" ")

stoneDict = {}

@cache
def calcNextStones(stone):
    temp = []
    stoneStr = str(stone)
    l = len(stoneStr)

    if(stone == 0):
        temp.append(1)
    elif (l % 2 == 0):
        l = int(l/2)
        stone1 = int(stoneStr[:l])
        stone2 = int(stoneStr[l:])
        temp.append(stone1)
        temp.append(stone2)
    else:
        temp.append(stone * 2024)

    return temp

for stone in stones:
    stone = int(stone)
    stoneDict[stone] = stoneDict.get(stone, 0) + 1

for i in range(75):
    stoneDictTemp = {}
    for stoneKey, stoneVal in stoneDict.items():
        Res = calcNextStones(stoneKey)
        for res in Res:
            stoneDictTemp[res] = stoneDictTemp.get(res, 0) + stoneVal
    stoneDict = stoneDictTemp.copy()
    if(i == 24):
        total1 = sum(stoneDict.values())
        print("Part1 : ", total1)
    
total2 = sum(stoneDict.values())
print("Part 2: ", total2)
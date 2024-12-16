import sys
import re

file = open("./day11/testinput.txt", "r")
content = file.read()
file.close()

stones = content.split(" ")

stoneDict = {}

def getNextStones(stone):
    global stoneDict
    temp = []
    if(type(stone) is list):
        print("Is List: ", stone)
        return 0
    elif(type(stone) is int):
        print("Is Int: ", stone)
        return 0
    if(stoneDict.get(stone) == None):
        l = len(stone)
        if(stone == "0"):
            temp.append("1")
        elif (l % 2 == 0):
            l = int(l/2)
            stone1 = stone[:l]
            stone2 = stone[l:]
            stone2 = str(int(stone2))
            temp.append(stone1)
            temp.append(stone2)
        else:
            temp.append(str(int(stone) * 2024))
        stoneDict[stone] = temp
    else:
        temp.extend(stoneDict[stone])

    return temp


print(stones)

for i in range(40):
    temp = []
    for stone in stones:
        temp.extend(getNextStones(stone))
    stones = temp

    if((i+1) % 5 == 0):
        print("Index ", i+1, ": ", len(stones))

#print("Part 2: ",len(stones))

#print(type(stones) is list)
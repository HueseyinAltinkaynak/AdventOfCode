import sys
import re

file = open("./day11/testinput.txt", "r")
content = file.read()
file.close()

stones = content.split(" ")

#print(stones)

for i in range(75):
    temp = []
    for stoneIndex in range(len(stones)):
        while(stones[stoneIndex][0] == "0" and len(stones[stoneIndex]) > 1):
            stones[stoneIndex] = stones[stoneIndex][1:]
        l = len(stones[stoneIndex])
        if(stones[stoneIndex] == "0"):
            temp.append("1")
        elif (l % 2 == 0):
            l = int(l/2)
            temp.append(stones[stoneIndex][:l])
            temp.append(stones[stoneIndex][l:])
        else:
            temp.append(str(int(stones[stoneIndex]) * 2024))
    stones = temp

    if((i+1) % 5 == 0):
        print("Index ", i+1, ": ", len(stones))

#print("Part 2: ",len(stones))
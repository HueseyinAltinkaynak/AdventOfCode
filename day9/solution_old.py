import sys
import re

file = open("./day9/input.txt", "r")
content = file.read()
file.close()

file = True
index = 0

compactDot = []

compactList = []

for char in content:
    if(file):
        for i in range(int(char)):
            compactDot.append(index)
            compactList.append(index)
        index += 1
    else:
        for i in range(int(char)):
            compactDot.append(".")
        #compact += "." * int(char)
    file = not file

index = 0

finalList = []
#print(compactList)
l = len(compactList)

while (len(finalList) < l):
    if(compactDot[index] == "."):
        lastList = compactList.pop()
        finalList.append(lastList)
        # last = compact[len(compact)-1]
        # while(last == "."):
        #     compact = compact[:len(compact)-1]
        #     last = compact[len(compact)-1]
        # compact = compact[:index] + last + compact[index+1:len(compact)-1]
    else:
        finalList.append(compactDot[index])
    index += 1

# for i in range(20):
#     print(i, finalList[i], i * finalList[i])

index = 0
total1 = 0

# for index in range(len(compact)):
#     total1 += index * int(compact[index])

for i in range((len(finalList))):
    total1 += i * finalList[i]

# print(compactDot)
# print(finalList)
print(total1)
# print(compact)
# print(finalList)

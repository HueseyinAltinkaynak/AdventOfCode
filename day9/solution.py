import sys
import re

file = open("./day9/testinput.txt", "r")
content = file.read()
file.close()

file = True
index = 0

compact = ""

compactList = []

for char in content:
    if(file):
        compact += str(index) * int(char)
        for i in range(int(char)):
            compactList.append(index)
        index += 1
    else:
        compact += "." * int(char)
    file = not file

index = 0

# Fehler da id nicht mehr einstellig

finalList = []

while (index < len(compact)):
    if(compact[index] == "."):
        lastList = compactList.pop()
        finalList.append(lastList)
        last = compact[len(compact)-1]
        while(last == "."):
            compact = compact[:len(compact)-1]
            last = compact[len(compact)-1]
        compact = compact[:index] + last + compact[index+1:len(compact)-1]
    else:
        finalList.append(int(compact[index]))
    index += 1

index = 0
total1 = 0

# for index in range(len(compact)):
#     total1 += index * int(compact[index])

for i in range(len(finalList)):
    total1 += i * finalList[i]

print(total1)
# print(compact)
# print(finalList)

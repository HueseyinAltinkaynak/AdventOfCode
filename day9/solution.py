import sys
import re

file = open("./day9/input.txt", "r")
content = file.read()
file.close()

file = True
index = 0

compact = ""

for char in content:
    if(file):
        compact += str(index) * int(char)
        index += 1
    else:
        compact += "." * int(char)
    file = not file

index = 0

# Fehler da id nicht mehr einstellig

while (index < len(compact)):
    if(compact[index] == "."):
        last = compact[len(compact)-1]
        while(last == "."):
            compact = compact[:len(compact)-1]
            last = compact[len(compact)-1]
        compact = compact[:index] + last + compact[index+1:len(compact)-1]
    index += 1

index = 0
total1 = 0

for index in range(len(compact)):
    total1 += index * int(compact[index])


print(total1)

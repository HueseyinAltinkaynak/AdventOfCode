import sys
import re

file = open("./day4/testinput.txt", "r")
content = file.read()
file.close()

lines = content.split("\n")

directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

maxLine = len(lines)-1
maxPos = len(lines[0])-1

total = 0

print(lines[maxLine][maxPos])

for line in range(maxLine):
  for pos in range(maxPos):
    if(lines[line][pos] == "X"):
      for dir in directions:
        vlim = line + 3* dir[0]
        hlim = pos + 3* dir[1]
        if (vlim < 0 or vlim > maxLine or hlim < 0 or hlim > maxPos):
          test = 0
        else:
          if (lines[line + dir[0]][pos + dir[1]] == "M"):
            if (lines[line + 2*dir[0]][pos + 2*dir[1]] == "A"):
              if (lines[line + 3*dir[0]][pos + 3*dir[1]] == "S"):
                total += 1

print(total)

import sys
import re

content = ""

for line in sys.stdin:
  content += line

lines = content.split("\n")
lines.pop()

directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

maxLine = len(lines)
maxPos = len(lines[0])

total = 0

for line in range(maxLine):
  for pos in range(maxPos):
    if(lines[line][pos] == "X"):
      for dir in directions:
        vlim = line + 3* dir[0]
        hlim = pos + 3* dir[1]
        if (vlim < 0 or vlim > maxLine-1 or hlim < 0 or hlim > maxPos-1):
          continue
        else:
          if (lines[line + dir[0]][pos + dir[1]] == "M"):
            if (lines[line + 2*dir[0]][pos + 2*dir[1]] == "A"):
              if (lines[line + 3*dir[0]][pos + 3*dir[1]] == "S"):
                total += 1

total2 = 0

for line in range(maxLine-1):
  if (line == 0):
    continue
  for pos in range(maxPos-1):
    if (pos == 0):
      continue
    if(lines[line][pos] == "A"):
      if (((lines[line-1][pos-1] == "M" and lines[line+1][pos+1] == "S") or (lines[line-1][pos-1] == "S" and lines[line+1][pos+1] == "M")) and ((lines[line-1][pos+1] == "M" and lines[line+1][pos-1] == "S") or (lines[line-1][pos+1] == "S" and lines[line+1][pos-1] == "M"))):
        total2 += 1


print("Part 1: ", total)
print("Part 2: ", total2)
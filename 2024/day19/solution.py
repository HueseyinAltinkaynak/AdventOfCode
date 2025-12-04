import sys
import re
import math

file = open("./day19/input.txt", "r")
content = file.read()
file.close()

split = content.split("\n\n")

towels = split[0].split(", ")
combos = split[1].split("\n")

def getCombo(comboStr):
	index = 0
	comboList = []
	while(index < len(towels)):
		part = towels[index]
		if(part == comboStr[:len(part)]):
			if(len(part) == len(comboStr)):
				return [part]
			else:		
				reslist = getCombo(comboStr[len(part):])
				if(reslist == []):
					index += 1
					continue
				else:
					comboList.append(part)
					comboList.extend(reslist)
					return comboList
		else:
			index += 1
			continue
	return comboList

total1 = 0

for combo in combos:
	if(len(getCombo(combo)) > 0):
		total1 += 1

print("Part 1 : ", total1)

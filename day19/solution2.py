import sys
import re
import math

file = open("./day19/testinput.txt", "r")
content = file.read()
file.close()

split = content.split("\n\n")

towels = split[0].split(", ")
comb = split[1].split("\n")

white = []
black = []
red = []
green = []
blue = []

for towel in towels:
	if(towel[0] == "w"):
		white.append(towel)
	elif(towel[0] == "b"):
		black.append(towel)
	elif(towel[0] == "r"):
		red.append(towel)
	elif(towel[0] == "g"):
		green.append(towel)
	elif(towel[0] == "u"):
		blue.append(towel)

def getComb(comboStr, index):
	l = len(comboStr)
	firstChar = comboStr[0]
	charCol = colList(firstChar)
	comboList = []
	part = ""
	found = False
	while(index < len(charCol)):
		part = charCol[index]

		if(len(part) > len(comboStr)):
			index += 1
			continue
		else:
			if(part == comboStr[:len(part)]):
				comboList.append(part)
				res = getComb(comboStr[len(part):], )
  

def colList(col):
  if(col == "e"):
    collist = white.copy()
  elif(col == "b"):
    collist = black.copy()
  elif(col == "r"):
    collist = red.copy()
  elif(col == "g"):
    collist = green.copy()
  elif(col == "u"):
    collist = blue.copy()
  else:
    collist = None
  return collist
  

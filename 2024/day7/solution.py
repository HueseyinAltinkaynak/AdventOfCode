import sys
import re

file = open("./day7/input.txt", "r")
content = file.read()
file.close()

def changeMode(m):
    if (m == "+"):
        return "*"
    else:
        return "+"

def check(line):
    s = line.split(": ")
    goal = int(s[0])
    steps = s[1].split(" ")
    start = int(steps[0])
    steps.pop(0)

    comb = ["0", "1"]

    for i in range(len(steps)-1):
        test = []
        for c in comb:
            test.append(c+"0")
            test.append(c+"1")
        comb = test

    for c in comb:
        total = start
        for i in range(len(c)):
            if(c[i] == "0"):
                total += int(steps[i])
            else:
                total *= int(steps[i])
        if(total == goal):
            return goal
        
    return 0

def check2(line):
    s = line.split(": ")
    goal = int(s[0])
    steps = s[1].split(" ")
    start = int(steps[0])
    steps.pop(0)

    comb = ["0", "1", "2"]

    for i in range(len(steps)-1):
        test = []
        for c in comb:
            test.append(c+"0")
            test.append(c+"1")
            test.append(c+"2")
        comb = test

    for c in comb:
        total = start
        for i in range(len(c)):
            if(c[i] == "0"):
                total += int(steps[i])
            elif(c[i] == "1"):
                total *= int(steps[i])
            else:
                total = int(str(total) + steps[i])
        if(total == goal):
            return goal
        
    return 0



lines = content.split("\n")

total1 = 0

for line in lines:
    total1 += check(line)

total2 = 0

for line in lines:
    total2 += check2(line)

print("Part 1: ", total1)
print("Part 2: ", total2)
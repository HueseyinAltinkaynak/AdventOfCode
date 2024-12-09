import sys
import re

file = open("./day7/testinput.txt", "r")
content = file.read()
file.close()

def check(line):
    s = line.split(": ")
    goal = int(s[0])
    steps = s[1].split(" ")
    total = int(steps[0])
    steps.pop(0)
    for step in steps:
        operator
    print(goal)
    print(steps)
    return total


lines = content.split("\n")

print(int(["1", "2"]))
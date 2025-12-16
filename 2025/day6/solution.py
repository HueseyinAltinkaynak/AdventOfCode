import os
import math

base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir, 'input.txt')

file = open(file_path, "r")
content = file.read()
file.close()
content_split = content.split("\n")

math_lines = []

for line in content_split:
    line_split = line.split(" ")
    ind = 0
    while(ind < len(line_split)):
        if line_split[ind] == "":
            line_split.pop(ind)
        else:
            ind +=1
    math_lines.append(line_split)

def calc(id):
    calc_mode = math_lines[len(math_lines)-1][id]
    total = 0
    if calc_mode == "+":
        total = 0
        for counter in range(len(math_lines)-1):
            total += int(math_lines[counter][id])
    elif calc_mode == "*":
        total = 1
        for counter in range(len(math_lines)-1):
            total *= int(math_lines[counter][id])
    
    return total

totalA = 0

for calcul in range(len(math_lines[0])):
    totalA += calc(calcul)


print(totalA)
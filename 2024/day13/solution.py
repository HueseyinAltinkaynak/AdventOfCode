import sys
import re

file = open("./day13/input.txt", "r")
content = file.read()
file.close()

machines = content.split("\n\n")

def calcLin(ax, ay, bx, by, X, Y):
    B = ((X*ay) - (Y*ax))/((bx*ay) - (by*ax))
    if(B > 0 and (int(B) == B)):
        A = (X - B * bx) / ax
        if(A > 0 and (int(A) == A)):
            return(int(A), int(B))
    return(0, 0)

total1 = 0
total2 = 0
first = True

for machine in machines:
    lines = machine.split("\n")
    lineA = lines[0].split("+")
    ax = int(lineA[1].replace(", Y", ""))
    ay = int(lineA[2])
    lineB = lines[1].split("+")
    bx = int(lineB[1].replace(", Y", ""))
    by = int(lineB[2])
    lineS = lines[2].split("=")
    X = int(lineS[1].replace(", Y", ""))
    Y = int(lineS[2])
    offset = 10000000000000
    sol = calcLin(ax, ay, bx, by, X, Y)
    sol2 = calcLin(ax, ay, bx, by, X + offset, Y + offset)
    total1 += 3 * sol[0] + sol[1]
    if(first):
        first = False
        continue
    total2 += 3 * sol2[0] + sol2[1]


print("Part 1: ", total1)
print("Part 2: ", total2)
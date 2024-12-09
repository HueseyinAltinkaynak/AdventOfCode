import sys
import re

file = open("./day8/input.txt", "r")
content = file.read()
file.close()

map = content.split("\n")
yMax = len(map)
xMax = len(map[0])

antennas = {}

for y in range(yMax):
    for x in range(xMax):
        pos = map[y][x]
        if(pos != "."):
            if(antennas.get(pos) == None):
                antennas[pos] = [(y, x)]
            else:
                antennas[pos].append((y, x))

nodes = []

for freq in antennas:
    for firstIndex in range(len(antennas[freq])):
        for secondIndex in range(firstIndex + 1, len(antennas[freq])):
            node = (antennas[freq][firstIndex][0] * 2 - antennas[freq][secondIndex][0], antennas[freq][firstIndex][1] * 2 - antennas[freq][secondIndex][1])
            if(-1 < node[0] and node[0] < yMax and -1 < node[1] and node[1] < xMax and node not in nodes):
                nodes.append(node)

            node = (antennas[freq][secondIndex][0] * 2 - antennas[freq][firstIndex][0], antennas[freq][secondIndex][1] * 2 - antennas[freq][firstIndex][1])
            if(-1 < node[0] and node[0] < yMax and -1 < node[1] and node[1] < xMax and node not in nodes):
                nodes.append(node)

            
print("Part 1: ", len(nodes))

for freq in antennas:
    for firstIndex in range(len(antennas[freq])):
        for secondIndex in range(firstIndex + 1, len(antennas[freq])):
            vector = (antennas[freq][secondIndex][0] - antennas[freq][firstIndex][0], antennas[freq][secondIndex][1] - antennas[freq][firstIndex][1])
            base = (antennas[freq][firstIndex][0], antennas[freq][firstIndex][1])
            while(-1 < node[0] and node[0] < yMax and -1 < node[1] and node[1] < xMax and node not in nodes):
                if(node not in nodes)
                nodes.append(node)

            node = (antennas[freq][secondIndex][0] * 2 - antennas[freq][firstIndex][0], antennas[freq][secondIndex][1] * 2 - antennas[freq][firstIndex][1])
            if(-1 < node[0] and node[0] < yMax and -1 < node[1] and node[1] < xMax and node not in nodes):
                nodes.append(node)

print("Part 2: ", len(nodes))                
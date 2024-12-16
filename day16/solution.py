import sys
import re

file = open("./day15/input.txt", "r")
content = file.read()
file.close()

map = content.split("\n")

wallList = []
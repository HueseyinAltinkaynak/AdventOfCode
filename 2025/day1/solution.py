import os

base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir, 'input.txt')

file = open(file_path, "r")
content = file.read()
file.close()
lines = content.split("\n")

pos = 50
old_pos = pos
count_0A = 0
count_0B = 0

l_dir = "R"
l_amount = 0

for line in lines:

    old_pos = pos
    l_dir = line[0]
    l_amount = int(line[1:])
            
    if pos == 0:
        count_0A += 1

    if l_dir == "R":
        pos += l_amount

        while(pos > 99):
            pos -= 100
            count_0B += 1
    elif l_dir == "L":
        pos -= l_amount
            
        while(pos < 0):
            pos += 100
            count_0B += 1

        if pos == 0:
            count_0B += 1

        if old_pos == 0:
            count_0B -= 1


print(count_0A)
print(count_0B)
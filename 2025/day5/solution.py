import os
import math

base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir, 'input.txt')

file = open(file_path, "r")
content = file.read()
file.close()
map_grid = content.split("\n")

max_y_index = len(map_grid)-1 
max_x_index = len(map_grid[0])-1 

def check_valid_roll(x,y):
    surrounded_rolls = 0    
    for y_range in range(-1, 2):
        for x_range in range(-1, 2):
            if y+y_range < 0 or y+y_range > max_y_index:
                continue
            elif x+x_range < 0 or x+x_range > max_x_index:
                continue
            elif x_range == 0 and y_range == 0:
                continue
            else:
                if(map_grid[y+y_range][x+x_range] == '@' or map_grid[y+y_range][x+x_range] == 'x'):
                    surrounded_rolls += 1

    return surrounded_rolls

def remove_rolls():
    removed_rolls = 0
    for y_pos in range(max_y_index+1):
        for x_pos in range(max_x_index+1):
            if(map_grid[y_pos][x_pos] == '@'):
                if(check_valid_roll(x_pos, y_pos) < 4):
                    # map_grid[y_pos][x_pos] = "."
                    map_grid[y_pos] = map_grid[y_pos][:x_pos]+"x"+map_grid[y_pos][x_pos+1:]
                    removed_rolls +=1

    for line_index in range(max_y_index+1):
        map_grid[line_index] = map_grid[line_index].replace("x", ".")

    return removed_rolls

index = 1
removable_rolls = 0

total_removed_rolls = 0

last_removed_rolls = -1

while (last_removed_rolls != 0):
    last_removed_rolls = remove_rolls()
    total_removed_rolls += last_removed_rolls

    if index == 1:
        removable_rolls = last_removed_rolls
        index = 2

print(removable_rolls)
print(total_removed_rolls)

# print("12343"[6:])

# for line in map_grid:
#     print(line)

# print("----------------")

# map_grid[0] = map_grid[0][:3-1]+"."+map_grid[0][3:]

# for line in map_grid:
#     print(line)
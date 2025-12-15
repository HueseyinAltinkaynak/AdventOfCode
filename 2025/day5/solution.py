import os
import math

base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir, 'input.txt')

file = open(file_path, "r")
content = file.read()
file.close()
content_split = content.split("\n\n")
range_list = content_split[0].split("\n")
id_list = content_split[1].split("\n")

for ind in range(len(range_list)):
    range_split = range_list[ind].split("-")
    range_list[ind] = (int(range_split[0]),int(range_split[1]))

def fresh_id(id_val):
    for r in range_list:
        if id_val >= r[0] and id_val <= r[1]:
            return True
    return False

last_range = range_list.pop()

range_list_clean = [(last_range[0],'S'),(last_range[1],'E')]

for r in range_list:
    temp_list = []
    for i in range(len(range_list_clean)):
        if range_list_clean[i][0] > r[0]:
            temp_list.extend(range_list_clean[:i])
            temp_list.append((r[0],'S'))
            temp_list.extend(range_list_clean[i:])
            break
        elif i == len(range_list_clean)-1:
            temp_list.extend(range_list_clean)
            temp_list.append((r[0],'S'))
    range_list_clean = temp_list
    temp_list = []
    for j in range(len(range_list_clean)):
        if range_list_clean[j][0] > r[1]:
            temp_list.extend(range_list_clean[:j])
            temp_list.append((r[1],'E'))
            temp_list.extend(range_list_clean[j:])
            break
        elif j == len(range_list_clean)-1:
            temp_list.extend(range_list_clean)
            temp_list.append((r[1],'E'))
    range_list_clean = temp_list

# range_list_clean.extend(range_list)

counter = 0

while (counter < len(range_list_clean)):
    if(range_list_clean[counter][1] == 'S' and range_list_clean[counter+1][1] == 'S' and range_list_clean[counter+2][1] == 'E'):
        range_list_clean.pop(counter+2)
        range_list_clean.pop(counter+1)
        counter = 0
        # print(range_list_clean)
    else:
        # print(counter)
        counter += 1

counter2 = 0

while counter2 < len(range_list_clean)-1:
    if counter2 % 2 == 1 and range_list_clean[counter2][0] == range_list_clean[counter2+1][0]:
        range_list_clean.pop(counter2+1)
        range_list_clean.pop(counter2)
    else:
        counter2 += 1

totalB = 0

range_list2 = []

for ranges in range_list_clean:
    if ranges[1] == 'S':
        totalB -= ranges[0]
        range_list2.append([ranges[0]])
    else:
        totalB += ranges[0]+1
        range_list2[len(range_list2)-1].append(ranges[0])



def fresh_id2(id_val):
    for r in range_list2:
        if id_val >= r[0] and id_val <= r[1]:
            return True
    return False

totalA = 0

for id in id_list:
    id_val = int(id)
    if fresh_id2(id_val):
        totalA +=1

print(totalA)
print(totalB)
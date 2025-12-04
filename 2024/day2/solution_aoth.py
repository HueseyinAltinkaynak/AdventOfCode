# file = open("./advent of code/day2/input_freddy.txt", "r")
# input = file.read()
# file.close()

#input = input()

#lines = input.split("\n")

import sys

def check_list(list, joker):
    for i in range(len(list)):
        if (i==0):
            if (abs(list[0]) < 1 or abs(list[0]) > 3 or list[0] * list[1] <= 0):
                if(joker):
                    list2 = list.copy()
                    list2.pop(0)
                    if (check_list(list2, False)):
                        return True
                else:
                    return False
        else:
            if (abs(list[i]) < 1 or abs(list[i]) > 3 or list[i] * list[i-1] <= 0):
                if(joker):
                    list2 = list.copy()
                    list2[i] += list2[i-1]
                    list2.pop(i-1)
                    if (check_list(list2, False)):
                        return True
                else:
                    return False
    if(joker):
      list3 = list.copy()
      list3.pop(len(list3)-1)
      return check_list(list3, False)

    return True


total = 0
total2 = 0


for line in sys.stdin:
#while (line != ""):
    s = line.split(" ")
    #line = ""
    l = []

    for i in range(len(s) - 1):
        l.append(int(s[i+1]) - int(s[i]))
            
    if (check_list(l, False)):
        total += 1
    if (check_list(l, True)):
        total2 += 1

print("Part 1: ", total)
print("Part 2: ", total2)
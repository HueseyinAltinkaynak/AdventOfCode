file = open("./day2/input.txt", "r")
content = file.read()
file.close()
lines = content.split("\n")


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
                    list3 = list.copy()
                    if(i==len(list)-1):
                        list3.pop(i)
                    else:
                        list3[i] += list3[i+1]
                        list3.pop(i+1)
                    return (check_list(list2, False) or check_list(list3, False))
                else:
                    return False

    return True


total = 0
total2 = 0


for line in lines:
    s = line.split(" ")
    l = []

    for i in range(len(s) - 1):
        l.append(int(s[i+1]) - int(s[i]))
            
    if (check_list(l, False)):
        total += 1
    if (check_list(l, True)):
        total2 += 1

print(total)
print(total2)
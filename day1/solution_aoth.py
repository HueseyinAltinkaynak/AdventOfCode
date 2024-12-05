import sys


# file = open("./day1/input.txt", "r")
# content = file.read()
# file.close()
# lines = content.split("\n")

total = 0
total2 = 0

l1 = []
l2 = []

for line in sys.stdin:
    s = line.split("   ")
    l1.append(int(s[0]))
    l2.append(int(s[1]))

l1.sort()
l2.sort()

for i in range(len(l1)):
    total += abs(l1[i]-l2[i])
    for j in range(len(l2)):
        if (l1[i] == l2[j]):
            total2 += l1[i]
        elif (l1[i] < l2[j]):
            break



print("Part 1:", total)
print("Part 2:", total2)
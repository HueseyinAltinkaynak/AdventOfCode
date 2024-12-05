import sys

content = sys.stdin.read()

lines = content.split("\n")
lines.pop()

total = 0
total2 = 0

l1 = []
l2 = []
d1 = {}
d2 = {}

for line in lines:
    s = line.split("   ")
    l1.append(int(s[0]))
    l2.append(int(s[1]))
    if (d1.get(s[0]) == None):
        d1[s[0]] = 1
    else:
        d1[s[0]] += 1
    if (d2.get(s[1]) == None):
        d2[s[1]] = 1
    else:
        d2[s[1]] += 1

l1.sort()
l2.sort()

for i in range(len(l1)):
    total += abs(l1[i]-l2[i])

for num in d1:
    if (d2.get(num) == None):
        test = 0
    else:
        total2 += d1[num] * d2[num] * int(num)

print(total)
print(total2)
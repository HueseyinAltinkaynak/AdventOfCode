import os
import math

base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir, 'input.txt')

file = open(file_path, "r")
content = file.read()
file.close()
banks = content.split("\n")

total = 0
bankTotal = ""
pos1 = 0
pos2 = 0

oldpos = -1
pos = -1

digit_num = 12 # 2 for part 1

for bank in banks:
    # print("--------------")
    # print("bank: "+bank)
    oldpos = -1
    pos = -1
    bankTotal = ''

    for digit in range(0,digit_num):
        oldpos += pos+1
        # print("oldpos: "+str(oldpos))
        for i in range(0, 10):
            val = str(9-i)
            pos = bank[oldpos+1:len(bank)-digit_num+1+digit].find(val)
            if pos == -1:
                continue
            else:
                bankTotal += bank[pos+oldpos+1]
                break
    # print(bankTotal)
    total += int(bankTotal)

print("Total Count: "+ str(total))
import re
import sys

# file = open("./day3/input.txt", "r")
# originalInput = file.read()
# file.close()

def computeMul(mulString):
    valid = True
    curnum = 1
    numstring1 = ""
    numstring2 = ""
    num1 = 0
    num2 = 0
    for char in mulString[4:]:
        if (curnum == 1):
            if(re.search("\d", char) != None):
                numstring1 += char
            elif(re.search(",", char) != None):
                num1 = int(numstring1)
                if(num1 > 999):
                    valid = False
                    break
                curnum = 2
            else:
                valid = False
                break
        elif (curnum == 2):
            if(re.search("\d", char) != None):
                numstring2 += char
            elif(re.search("\)", char) != None):
                num2 = int(numstring2)
                if(num2 > 999):
                    valid = False
                    break
                break
            else:
                valid = False
                break
    
    if (valid):
        return num1 * num2
    else:
        return 0

total = 0
total2 = 0

for line in sys.stdin:
    input = line

    index = re.search("mul\(", input)

    while(index != None):
        mulString = input[index.start():index.start()+12]
        total += computeMul(mulString)
        input = input[index.start()+4:]
        index = re.search("mul\(", input)



    input = line

    indexDont = re.search("don't\(\)", input)

    while(indexDont != None):
        indexDo = re.search("do\(\)", input)
        if (indexDo != None):
            while(indexDo.start() < indexDont.start()):
                input = input[:indexDo.start()] + input[indexDo.end():]
                indexDont = re.search("don't\(\)", input)
                indexDo = re.search("do\(\)", input)
                if (indexDo == None):
                    break
            if (indexDo != None):
                input = input[:indexDont.start()] + input[indexDo.end():]
            else:
                input = input[:indexDont.start()]
        else:
            input = input[:indexDont.start()]
        indexDont = re.search("don't\(\)", input)


    

    index = re.search("mul\(", input)

    while(index != None):
        mulString = input[index.start():index.start()+12]
        total2 += computeMul(mulString)
        input = input[index.start()+4:]
        index = re.search("mul\(", input)

print("Part 1: ", total)
print("Part 2: ", total2)
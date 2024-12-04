import re

file = open("./day3/input.txt", "r")
input = file.read()
file.close()

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

index = re.search("mul\(", input)

while(index != None):
    mulString = input[index.start():index.start()+12]
    total += computeMul(mulString)
    input = input[index.start()+4:]
    index = re.search("mul\(", input)

print(total)
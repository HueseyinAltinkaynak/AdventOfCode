import sys
import re
import math

file = open("./day17/input.txt", "r")
content = file.read()
file.close()

inputStr = content.split("\n\n")
register = inputStr[0].split("\n")
regA = int(register[0][12:])
regB = int(register[1][12:])
regC = int(register[2][12:])
commands = inputStr[1][9:].split(",")
out = []

def getVal(operand, literal):
    if(literal or operand < 4):
        return operand
    elif(operand == 4):
        return regA
    elif(operand == 5):
        return regB
    elif(operand == 6):
        return regC

def bitwiseXOR(num1, num2):
    bit1 = bin(num1)[2:]
    bit2 = bin(num2)[2:]
    diff = len(bit1)-len(bit2)
    if(diff > 0):
        bit2 = "0" * diff + bit2
    elif(diff < 0):
        bit1 = "0" * (-diff) + bit1
    bitRes = ""
    for i in range(len(bit1)):
        if(bit1[i] == bit2[i]):
            bitRes += "0"
        else:
            bitRes += "1"
    bitRes = "0b" + bitRes
    return int(bitRes, 2)

def divA(operand):
    val = getVal(operand, False)
    return int(regA/math.pow(2, val))

def execFunc(pointer):
    global regA
    global regB
    global regC
    global out
    opcode = int(commands[pointer])
    operand = int(commands[pointer+1])
    nextPointer = pointer + 2
    if(opcode == 0):
        regA = divA(operand)
    elif(opcode == 1):
        val = getVal(operand, True)
        regB = bitwiseXOR(regB, val)
    elif(opcode == 2):
        val = getVal(operand, False)
        regB = val % 8
    elif(opcode == 3):
        if(regA != 0):
            val = getVal(operand, True)
            nextPointer = val
    elif(opcode == 4):
        regB = bitwiseXOR(regB, regC)
    elif(opcode == 5):
        val = getVal(operand, False)
        val = val % 8
        out.append(val)
    elif(opcode == 6):
        regB = divA(operand)
    elif(opcode == 7):
        regC = divA(operand)
    return nextPointer

def runProgram1():
    pointer = 0

    while(pointer < len(commands)):
        pointer = execFunc(pointer)

    outVal = ""
    for val in out:
        outVal += "," + str(val)
    outVal = outVal[1:]
    print("Part 1: ", outVal)

def runProgram2():
    pointer = 0

    while(pointer < len(commands)):
        pointer = execFunc(pointer)

    outStr = []
    for val in out:
        outStr.append(str(val))
    out.clear()
    return(outStr)


Aval = 150000000
regA = 0
outPut = runProgram2()

while(outPut != commands):
    Aval += 1
    regA = Aval
    outPut = runProgram2()
    if(Aval % 10000 == 0):
        print(Aval, end='\r')

print(Aval)

# for i in range(1000000000000000000000000000000000000000000000000000):
#     print(i, end='\r')
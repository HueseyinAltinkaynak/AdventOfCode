import os
import math

base_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_dir, 'input.txt')

file = open(file_path, "r")
content = file.read()
file.close()
ranges_list = content.split(",")

id_list = []
total = 0

for range_val in ranges_list:
    # print("***********************")
    # print(range_val)

    vals = range_val.split("-")
    range_start = int(vals[0])
    range_end = int(vals[1]) + 1

    # print(type(range_start))
    # print(type(range_end))
    for val in range(range_start, range_end): # go through the ranges
        # print("-----------------------")
        # print("Current Value: "+str(val))
        string_val = str(val)
        string_len = len(string_val)
        for i in range(1,math.floor(string_len/2)+1): # go through the possible dividers
            if string_len % i == 0: # check if the current divider gets remainder 0 (clean divider)
                # print(str(i)+" is a clean multiple of "+str(string_len))
                for j in range(2, int(string_len/i)+1): # go through the possible multiples
                    # print("Comparing "+string_val[:i]+" with "+string_val[i*(j-1):i*j])
                    if string_val[:i] == string_val[i*(j-1):i*j]:
                        if j == int(string_len/i):
                            #print("Value added "+str(val))
                            if val not in id_list:
                                # print("Value added "+str(val))
                                id_list.append(val)
                            # total += val
                    else:
                        # print("Value dismissed")
                        break
            else:
                # print(str(i)+" is not a clean multiple of "+str(string_len))
                continue
        # print("Value: "+string_val)
        # print("Total: "+str(total))

    #l_len = len("abcd")
    
    #print()

for id in id_list:
    total += id

print("Total Count: "+ str(total))
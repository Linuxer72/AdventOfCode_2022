from time import perf_counter as pfc
from collections import Counter

start = pfc()
#choose_vs_points = {"AY": 8, "AZ": 3, "AX": 4, "BZ": 9, "BX": 1, "BY": 5, "CX": 7, "CY": 2, "CZ": 6}  ## Rules Play_1 from Inputtext
with open ("input.txt") as f:
    data = [x.replace(" ", "") for x in f.read().strip().split("\n")]

##########  Part 1  #################################################    
values = Counter(data)
sum_value_list = []
for value in values:
    if value == "AY":
        sum_value_list.append(values["AY"]*8)
    elif value == "AZ":
        sum_value_list.append(values["AZ"]*3)
    elif value == "AX":
        sum_value_list.append(values["AX"]*4)
    elif value == "BZ":
        sum_value_list.append(values["BZ"]*9)
    elif value == "BX":
        sum_value_list.append(values["BX"])
    elif value == "BY":
        sum_value_list.append(values["BY"]*5)
    elif value == "CX":
        sum_value_list.append(values["CX"]*7)
    elif value == "CY":
        sum_value_list.append(values["CY"]*2)
    elif value == "CZ":
        sum_value_list.append(values["CZ"]*6)
    else:
        print("Nothing ...")
                                                                                                       
res = sum(sum_value_list)
print("Part_1: ", res)  

######################################################################
##############  Part 2  ##############################################

#choose_vs_points = {"AY": 4, "AZ": 8, "AX": 3, "BZ": 9, "BX": 1, "BY": 5, "CX": 2, "CY": 6, "CZ": 7}  ## Rules Play_2 from Inputtext
sum_value_list_2 = []
for value in values:
    if value == "AY":
        sum_value_list_2.append(values["AY"]*4)
    elif value == "AZ":
        sum_value_list_2.append(values["AZ"]*8)
    elif value == "AX":
        sum_value_list_2.append(values["AX"]*3)
    elif value == "BZ":
        sum_value_list_2.append(values["BZ"]*9)
    elif value == "BX":
        sum_value_list_2.append(values["BX"]*1)
    elif value == "BY":
        sum_value_list_2.append(values["BY"]*5)
    elif value == "CX":
        sum_value_list_2.append(values["CX"]*2)
    elif value == "CY":
        sum_value_list_2.append(values["CY"]*6)
    elif value == "CZ":
        sum_value_list_2.append(values["CZ"]*7)
    else:
        print("Nothing ...")
      
res_2 = sum(sum_value_list_2)
print("Part_2: ", res_2)
print("Time: ", (pfc()-start), "sec")

from time import perf_counter as pfc
from collections import Counter

start = pfc()
choose_vs_points = {"AY": 8, "AZ": 3, "AX": 4, "BZ": 9, "BX": 1, "BY": 5, "CX": 7, "CY": 2, "CZ": 6}  ## Rules Play_1 from Inputtext
with open ("input.txt") as f:
    data = [x.replace(" ", "") for x in f.read().strip().split("\n")]

##########  Part 1  #################################################    
values = Counter(data)
sum_value_list = []

for k, v in choose_vs_points.items():
    for key, value in values.items():
        if k == key:
            sum_value_list.append(values[key] * choose_vs_points[k])

res = sum(sum_value_list)
print("Part_1: ", res)  

######################################################################
##############  Part 2  ##############################################

choose_vs_points_2 = {"AY": 4, "AZ": 8, "AX": 3, "BZ": 9, "BX": 1, "BY": 5, "CX": 2, "CY": 6, "CZ": 7}  ## Rules Play_2 from Inputtext
sum_value_list_2 = []

for k, v in choose_vs_points_2.items():
    for key, value in values.items():
        if k == key:
            sum_value_list_2.append(values[key] * choose_vs_points_2[k])
                     
res_2 = sum(sum_value_list_2)
print("Part_2: ", res_2)
print("Berechnungsdauer: ", (pfc()-start), "Sekunden")

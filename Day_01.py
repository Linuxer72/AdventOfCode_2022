from time import perf_counter as pfc
###########  Part 1  ############################################
### Elf with most carrying Calories  ############################
start = pfc()
with open ("input.txt") as f:
    data = f.read()
    data_new = list(x.split("\n") for x in data.split("\n\n"))
    for i in range (0, len(data_new)):
        for j in  range (0, len(data_new[i])):
            data_new[i][j] = int(data_new[i][j])                   
   
max_value = [sum(x) for x in data_new]
print(max(max_value))

#################################################################

##########  Part 2  #############################################
### Elfs with most three Calories - sum Calories ################

max_value_sort = sorted(max_value)  
max_value = [sum(x) for x in data_new]
most_three = []
for i in range (3):
    value = max(max_value)
    most_three.append(value)
    max_value.remove(value)

print(sum(most_three))
print(pfc()-start)

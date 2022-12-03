from time import perf_counter as pfc

start = pfc()
###############################  Part 1  #####################################
values = []
char_list = []
num_list = []
three_elves_groups = []
UpperList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
with open ("input.txt") as f:
    raw_data = f.read().split()    
    for i in raw_data:
        value = (i[:len(i)//2], i[len(i)//2:])
        values.append(value)
        
for val in values:
    for char in val[0]:
        if char in val[1]:
            char_list.append(char)
            break
            
for item in char_list:
    for i, char in enumerate(UpperList):
        if char == item:
            num_list.append(i+27)                                                                         
        if char.lower() == item:
            num_list.append(i+1)
              
print("Part_1: ", sum(num_list))

############################### Part 2  ########################################
for i in range(0, len(raw_data),3):
    group = [raw_data[i], raw_data[i+1], raw_data[i+2]]
    three_elves_groups.append(group)

 
new_list_char = []
for i in three_elves_groups:
    a, b, c = set(i[0]), set(i[1]), set(i[2])
    d = (a & b & c).pop()
    new_list_char.append(d)
            
new_list_num = []
for item in new_list_char:
    for i, char in enumerate(UpperList):
        if char == item:
            new_list_num.append(i+27)                                                                         
        if char.lower() == item:
            new_list_num.append(i+1)    
   
print("Part_2: ", sum(new_list_num))    
print("Berechnungsdauer: ", (pfc()-start), "Sekunden")

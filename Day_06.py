from time import perf_counter as pfc

start = pfc()

with open ("input.txt") as f:
    data = f.read()
    
########  Part 1  ###################
def search_of_four(data):
    for i in range(0, len(data)-4):
        chars = set()
        for j in range(4):
            chars.add(data[i+j])
        if len(chars) == 4:
            return (i+j)+1
#####################################
#########  Part 2  ##################        
def search_of_fourteen(data):
    for i in range(0, len(data)-14):
        chars = set()
        for j in range(14):
            chars.add(data[i+j])
        if len(chars) == 14:
            return (i+j)+1        
        
        
print("Part_1: ", search_of_four(data))
print("Part_2: ", search_of_fourteen(data))
print("Time: ", (pfc()-start), "seconds")

from time import perf_counter as pfc

start = pfc()

with open ("input.txt") as f:
    data = f.read()
    
#########  Part 1 & 2  ##################        
def search_of_(data, length):
    for i in range(0, len(data)-length):
        chars = set()
        for j in range(length):
            chars.add(data[i+j])
        if len(chars) == length:
            return (i+j)+1        
        
        
print("Part_1: ", search_of_(data, 4))
print("Part_2: ", search_of_(data, 14))
print("Time: ", (pfc()-start), "seconds")

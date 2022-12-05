from time import perf_counter as pfc

start = pfc()

with open ("input.txt") as f:
    data = f.readlines()
    data = [x.split() for x in data][10:]
    for i in data:
        i.remove("move")
        i.remove("from")
        i.remove("to")
    
res = ""
res1 = ""
places = [["R", "Q", "G", "P", "C", "F"],
         ["P", "C", "T", "W"],
         ["C", "M", "P", "H", "B"],
         ["R", "P", "M", "S", "Q", "T", "L"],
         ["N", "G", "V", "Z", "J", "H", "P"],
         ["J", "P", "D"],
         ["R", "T", "J", "F", "Z", "P", "G", "L"],
         ["J", "T", "P", "F", "C", "H", "L", "N"],
         ["W", "C", "T", "H", "Q", "Z", "V", "G"]]

places1 = [["R", "Q", "G", "P", "C", "F"],
          ["P", "C", "T", "W"],
          ["C", "M", "P", "H", "B"],
          ["R", "P", "M", "S", "Q", "T", "L"],
          ["N", "G", "V", "Z", "J", "H", "P"],
          ["J", "P", "D"],
          ["R", "T", "J", "F", "Z", "P", "G", "L"],
          ["J", "T", "P", "F", "C", "H", "L", "N"],
          ["W", "C", "T", "H", "Q", "Z", "V", "G"]]

#######   Functions  ##########
def moves(a, b, c, places):
    for i in range(a):
        places[c-1].insert(0, places[b-1][0])
        places[b-1].pop(0)
        #print(places1)
    return places

def moves1(a, b, c, places1):
    for i in range(a):
        places1[c-1].insert(i, places1[b-1][0])
        places1[b-1].pop(0)
    return places1
###############################

#####  Part_1  ########
for i in data:
    for k in range(0, len(data)):
        moves(int(data[k][0]), int(data[k][1]), int(data[k][2]), places)
    break

for i in places:
    for j in i:
        res += j
        break
    
#####  Part_2  ########
for i in data:
    for k in range(0, len(data)):
        moves1(int(data[k][0]), int(data[k][1]), int(data[k][2]), places1)
    break
     
for i in places1:
    for j in i:
        res1 += j
        break  
    
print("Part_1: ", res) 
print("Part_2: ", res1)
print("Time: ", (pfc()-start), "seconds")

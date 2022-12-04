from time import perf_counter as pfc

start = pfc()

with open ("input.txt") as f:
    data = [k.split(",") for k in (x.replace("-", ",") for x in f.read().strip().split())]
    
counter = 0
counter2 = 0
def compare(a, b, x, y):
    global counter
    val1, val2 = set(), set()
    for i in range(a, b+1):
        val1.add(i)
    for j in range(x, y+1):
        val2.add(j)
    if (val1 <= val2) or (val1 >= val2):
        counter +=1
    return counter

def compare2(a, b, x, y):
    global counter2
    val1, val2 = set(), set()
    for i in range(a, b+1):
        val1.add(i)
    for j in range(x, y+1):
        val2.add(j)
    if (val1 & val2):
        counter2 +=1
    return counter2
    
def send_values():
    for i in data:
        compare(int(i[0]), int(i[1]), int(i[2]), int(i[3]))
    for i in data:
        compare2(int(i[0]), int(i[1]), int(i[2]), int(i[3]))  
        
send_values()
print("Part_1: ", counter)
print("Part_2: ", counter2)
print("Time: ", (pfc()-start), "seconds")

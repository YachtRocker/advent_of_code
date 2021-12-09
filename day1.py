# advent of code for reddit
# this is working now.

total = 0
lst = []

file = open('day1number.txt', 'r')
lines = file.readlines()

for i in lines:
    lst.append(int(i))


def single_diff(li):
    total = 0
    for x, y in zip(li, li[1: ]):        
        if(x < y):
            total += 1   
        
    print(total)

def multiple_diff(li):
    total = 0
    tot_list = []
    for x, y, z in zip(li, li[1: ], li[2:]):        
        xyz = x + y + z
        tot_list.append(xyz)
        #print(xyz)

    for x, y in zip(tot_list, tot_list[1: ]):
        if (x < y):
            total += 1
    
    print(total)

single_diff(lst)
multiple_diff(lst)
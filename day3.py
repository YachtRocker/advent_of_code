from typing import Match


file = open('test.txt', 'r')
lines = file.readlines()


def part1(lines):
    gamma = [0, 0, 0, 0, 0]
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    count = 0
    total_lines = 0

    for ln in lines:
        total_lines += 1
        count = 0
        for b in ln:                        
            if count == 0 and int(b) == 1: 
                zero += 1 
            elif count == 1 and int(b) == 1: 
                    one += 1
            elif count == 2 and int(b) == 1: 
                    two += 1
            elif count == 3 and int(b) == 1:
                    three += 1
            elif count == 4 and int(b) == 1:
                    four += 1   

            count += 1   

    if zero > total_lines / 2:
        gamma[0] = 1
    if one > total_lines / 2:
        gamma[1] = 1
    if two > total_lines / 2:
        gamma[2] = 1
    if three > total_lines / 2:
        gamma[3] = 1
    if four > total_lines / 2:
        gamma[4] = 1

    print(zero, one, two, three, four)
    print(total_lines)
    
    return gamma

print(part1(lines))
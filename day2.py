file = open('day2text.txt', 'r')
lines = file.readlines()

def part1(lines):
    depth = 0
    horizontal = 0

    for cmd in lines:
        cmd = cmd.split()
        if cmd[0] == 'forward':
            horizontal += int(cmd[1])
        elif cmd[0] == 'up':
            depth -= int(cmd[1])
        elif cmd[0] == 'down':
            depth += int(cmd[1])
        
    print(depth, horizontal)
    print(horizontal * depth)

# part 2
def part2(lines):
    aim = 0
    horizontal = 0
    depth = 0

    for cmd in lines:
        cmd = cmd.split()
        if cmd[0] == 'forward':
            if aim == 0:
                horizontal += int(cmd[1])
            else:
                horizontal += int(cmd[1])
                depth += int(cmd[1]) * aim
        elif cmd[0] == 'up':
            aim -= int(cmd[1])
        elif cmd[0] == 'down':
            aim += int(cmd[1])
       #print(aim, horizontal, depth)        

    
    print(horizontal * depth)

part1(lines)
part2(lines)
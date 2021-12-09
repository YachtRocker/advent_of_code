file = open('day2text.txt', 'r')
lines = file.readlines()

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


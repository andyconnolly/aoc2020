t = ['F10', 'N3', 'F7', 'R90', 'F11']
d = [x.strip() for x in open("12input.txt", "r")]

def move(direction, value, pos):
    if direction == 'N':
        pos[1] += value
    elif direction == 'S':
        pos[1] -= value
    elif direction == 'E':
        pos[0] += value
    elif direction == 'W':
        pos[0] -= value
    return pos

def rotate(direction, value, pos):
    if direction == 'L':
         for x in range(value // 90):
             pos = [-pos[1], pos[0]]
    elif direction == 'R':
         for x in range(value // 90):
             pos = [pos[1], -pos[0]]
    return pos

def part1(data):
    instructions = [[x[0], int(x[1:])] for x in data]
    position = [0, 0]
    facing = [1, 0]
    for instruction in instructions:
        if instruction[0] in ('N', 'S', 'E', 'W'):
            position = move(instruction[0], instruction[1], position)
        elif instruction[0] in ('L', 'R'):
            facing = rotate(instruction[0], instruction[1], facing)
        elif instruction[0] == 'F':
            position = [position[0] + facing[0] * instruction[1], position[1] + facing[1] * instruction[1]]
    print(position, (manhattan_distance := abs(position[0]) + abs(position[1])))
    return manhattan_distance

def part2(data):
    instructions = [[x[0], int(x[1:])] for x in data]
    position = [0, 0]
    waypoint = [10, 1]
    for instruction in instructions:
        if instruction[0] in ('N', 'S', 'E', 'W'):
            waypoint = move(instruction[0], instruction[1], waypoint)
        elif instruction[0] in ('L', 'R'):
            waypoint = rotate(instruction[0], instruction[1], waypoint)
        elif instruction[0] == 'F':
            position = [position[0] + instruction[1] * waypoint[0], position[1] + instruction[1] * waypoint[1]]
    print(position, (manhattan_distance := abs(position[0]) + abs(position[1])))
    return manhattan_distance

print(part1(d))
print (part2(d))

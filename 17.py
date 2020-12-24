data = '.#.\n..#\n###\n'
data = open('17input.txt', 'r').read()

neighbours = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1) if (x, y, z) != (0, 0, 0)]
cubes = set()

for y in range(len(rows := data.split())):
    row = rows[y]
    for x in range(len(row)):
        col = row[x]
        if (col == '#'):
            cubes.add((x, y, 0))

def activeNeighbours(k, cubes):
    active = 0
    for n in neighbours:
        if (c := tuple(sum(x) for x in zip(k, n))) in cubes:
            active += 1
    return active

def cycle(cubes):
    new_cubes = set()
    min_x = min([x[0] for x in cubes])
    max_x = max([x[0] for x in cubes])
    min_y = min([x[1] for x in cubes])
    max_y = max([x[1] for x in cubes])
    min_z = min([x[2] for x in cubes])
    max_z = max([x[2] for x in cubes])
    
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                active = activeNeighbours((x, y, z), cubes)
                if active == 3:
                    new_cubes.add((x, y, z))
                elif active == 2 and (x, y, z) in cubes:
                    new_cubes.add((x, y, z))
    return new_cubes

for i in range(6):
    cubes = cycle(cubes)

print(len(cubes))


data = open('17input.txt', 'r').read()

neighbours = [(x, y, z, w) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1) for w in (-1, 0, 1) if (x, y, z, w) != (0, 0, 0, 0)]
cubes = set()

for y in range(len(rows := data.split())):
    row = rows[y]
    for x in range(len(row)):
        col = row[x]
        if (col == '#'):
            cubes.add((x, y, 0, 0))

def activeNeighbours(k, cubes):
    active = 0
    for n in neighbours:
        if (c := tuple(sum(x) for x in zip(k, n))) in cubes:
            active += 1
    return active

def cycle(cubes):
    new_cubes = set()
    min_x = min([x[0] for x in cubes])
    max_x = max([x[0] for x in cubes])
    min_y = min([x[1] for x in cubes])
    max_y = max([x[1] for x in cubes])
    min_z = min([x[2] for x in cubes])
    max_z = max([x[2] for x in cubes])
    min_w = min([x[3] for x in cubes])
    max_w = max([x[3] for x in cubes])
    
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                for w in range(min_w - 1, max_w + 2):
                    active = activeNeighbours((x, y, z, w), cubes)
                    if active == 3:
                        new_cubes.add((x, y, z, w))
                    elif active == 2 and (x, y, z, w) in cubes:
                        new_cubes.add((x, y, z, w))
    return new_cubes

for i in range(6):
    cubes = cycle(cubes)

print(len(cubes))

import re
instructions = [re.compile(r'(e|se|sw|w|nw|ne)').findall(x) for x in open('24input.txt', 'r')]
black_tiles = set()
move = { 'w': lambda x: x - 2,       'e': lambda x: x + 2, 
        'nw': lambda x: x - 1 + 1j, 'ne': lambda x: x + 1 + 1j, 
        'sw': lambda x: x - 1 - 1j, 'se': lambda x: x + 1 - 1j}

def part1(instructions, black_tiles):
    for instruction in instructions:
        pos = 0 + 0j 
        for direction in instruction:
            pos = move[direction](pos)
        black_tiles.remove(pos) if pos in black_tiles else black_tiles.add(pos)
    return len(black_tiles)

def part2(black_tiles):
    for i in range(100):
        neighbour_counts = dict()
        for tile in black_tiles:
            for fn in move.values():
                pos = fn(tile)
                neighbour_counts[pos] = neighbour_counts.get(pos, 0) + 1
        new_tiles = set()
        for tile, count in neighbour_counts.items():
            if tile in black_tiles and 0 < count <= 2:
                new_tiles.add(tile)
            elif tile not in black_tiles and count == 2:
                new_tiles.add(tile)
        black_tiles = new_tiles
    return len(black_tiles)

print('part 1:', part1(instructions, black_tiles))
print('part 2:', part2(black_tiles))

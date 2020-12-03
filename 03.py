d = [x.strip() for x in open("03input.txt", "r")]
test_data = ['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.', '..#.##.....', 
             '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#', '.#..#...#.#']

def part1(data, right, down):
    trees_encountered = 0
    width = len(data[0])
    height = len(data)
    x, y = (0, 0)
    for x in range(down, height, down):
        y = (y + right) % width
        if data[x][y] == '#':
            trees_encountered += 1
    return trees_encountered

def part2(data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for r, d in slopes:
        product *= part1(data, r, d)
    return product

print(part1(d, 3, 1))
print(part2(d))

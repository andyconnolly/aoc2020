d = ['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL', 
     'L.LLLLL.LL', '..L.L.....', 'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL']
d = [x.strip() for x in open("11input.txt", "r")]

def neighbours_occupied(seat, occupied):
    adjacent = ((-1+1j), -1, (-1-1j), 1j, -1j, (1+1j), 1, (1-1j))
    neighbours = 0
    for x in adjacent:
        if seat + x in occupied:
            neighbours += 1
    return neighbours

def directions_occupied(seat, seats, occupied, row_size, col_size):
    adjacent = ((-1+1j), -1, (-1-1j), 1j, -1j, (1+1j), 1, (1-1j))
    occ = 0
    for x in adjacent:
        processed = False
        pos = seat
        while not processed:
            pos += x
            if (0 <= pos.real < row_size) and (0 <= pos.imag < col_size):
                if pos in seats:
                    processed = True
                    if pos in occupied:
                        occ += 1
            else:
                processed = True
    return occ

def part1(data):
    seats = {complex(i, j) for i in range(len(data[0])) for j in range(len(data)) if data[j][i] != '.'}
    occupied = set()
    while True:
        new_occupied = {x for x in occupied}
        for seat in seats:
            if (seat not in occupied) and neighbours_occupied(seat, occupied) == 0:
                new_occupied.add(seat)
            elif (seat in occupied) and neighbours_occupied(seat, occupied) >= 4:
                new_occupied.remove(seat)
        if occupied == new_occupied:
            return len(occupied)
        occupied = new_occupied

def part2(data):
    seats = {complex(i, j) for i in range(len(data[0])) for j in range(len(data)) if data[j][i] != '.'}
    col_size = len(data)
    row_size = len(data[0])
    occupied = set()
    while True:
        new_occupied = {x for x in occupied}
        for seat in seats:
            if (seat not in occupied) and directions_occupied(seat, seats, occupied, row_size, col_size) == 0:
                new_occupied.add(seat)
            elif (seat in occupied) and directions_occupied(seat, seats, occupied, row_size, col_size) >= 5:
                new_occupied.remove(seat)
        if occupied == new_occupied:
            return len(occupied)
        occupied = new_occupied

print(part1(d))
print(part2(d))

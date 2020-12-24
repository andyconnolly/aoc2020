def part1(data):
    cups = [int(x) for x in data]
    L = len(cups)
    current_pos = 0
    for i in range(100):
        c1, c2, c3 = cups[(current_pos + 1) % L] , cups[(current_pos + 2) % L] , cups[(current_pos + 3) % L]
        dest_cup = cups[current_pos] - 1
        current_cup = cups[current_pos]
        cups.remove(c1)
        cups.remove(c2)
        cups.remove(c3)
        while dest_cup not in cups:
            dest_cup = dest_cup - 1 if dest_cup > 1 else 9 
        dest_pos = cups.index(dest_cup) + 1
        cups = cups[:dest_pos] + [c1, c2, c3] + cups[dest_pos:]
        current_pos = (cups.index(current_cup) + 1) % L
    cups = cups[cups.index(1) + 1:] + cups[:cups.index(1)]
    return(''.join([str(x) for x in cups]))

def part2(data):
    cups = [int(x) for x in data]
    L = len(cups)
    lookup = dict()
    for i in range(L - 1):
        lookup[cups[i]] = cups[i + 1]
    lookup[cups[L - 1]] = 10
    for i in range(L, 1000000):
        lookup[i + 1] = i + 2
    lookup[1000000] = cups[0]
    current_cup = cups[0]
    for i in range(10000000):
        c1 = lookup[current_cup]
        c2 = lookup[c1]
        c3 = lookup[c2]
        lookup[current_cup] = lookup[c3]
        dest_cup = 1000000 if current_cup == 1 else current_cup - 1
        while dest_cup in [c1,c2,c3]:
            dest_cup = 1000000 if dest_cup == 1 else dest_cup - 1
        lookup[c3] = lookup[dest_cup]
        lookup[dest_cup] = c1
        current_cup = lookup[current_cup]
    return(lookup[1] * lookup[lookup[1]] )

d = '167248359'
print(part1(d))
print(part2(d))

d = [x.strip() for x in open("13input.txt", "r")]

earliest_timestamp = int(d[0])
buses = [[i, int(x)] for i, x in enumerate(d[1].split(',')) if x != 'x']

def part1(buses, earliest_timestamp):
    timings = [[x, x - (earliest_timestamp % x)] for i, x in buses]
    bus_no = 0
    min_time = timings[0][1]
    for idx in range(1, len(timings)):
        if timings[idx][1] < min_time:
            bus_no, min_time = timings[idx]
    return bus_no * min_time

def part2(buses):
    period = 1
    time = 0
    for list_position, bus_no in buses:
        found = False
        while not found:
            if (time + list_position) % bus_no == 0: 
                found = True
            else:
                time += period
        period *= bus_no #increase in periods of products of previously found bus numbers
    return time

print('Part 1:', part1(buses, earliest_timestamp))
print('Part 2:', part2(buses))

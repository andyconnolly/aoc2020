d = open("06input.txt", "r").read().split('\n\n')

def part1(data):
    return sum([len(set(x.replace('\n',''))) for x in data])

def part2(data):
    sum = 0
    for item in data:
        common = {chr(x) for x in range(97,123)}
        for person in item.strip().split('\n'):
            common = common.intersection(set(person))
        sum += len(common)
    return sum

print(part1(d))
print(part2(d))

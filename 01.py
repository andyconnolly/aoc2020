d = [int(x) for x in open("01input.txt", "r")]

def part1(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]

def part2(data):
    for i in range(len(data) - 2):
        for j in range(i + 1, len(data) - 1):
            sum_ij = data[i] + data[j] 
            if sum_ij < 2020:
                for k in range(j + 1, len(data)):
                    if sum_ij + data[k] == 2020:
                        return data[i] * data[j] * data[k]

print(part1(d))
print(part2(d))

#Using list comprehensions instead:
[d[i] * d[j] for i in range(len(d) - 1) for j in range(i + 1, len(d)) if d[i] + d[j] == 2020][0]
[d[i] * d[j] * d[k] for i in range(len(d) - 2) for j in range(i + 1, len(d) - 1) for k in range(j + 1, len(d)) if d[i] + d[j] + d[k] == 2020][0]

#More efficient code
def find_pair(data, target):
    seen = set()
    for item in data:
        if target - item in seen:
            return (target - item) * item
        seen.add(item)

def find_triple(data, target):
    index = 2
    for item in data:
        if pair_product := find_pair(data[:index], target - item):
            return pair_product * item
        index += 1

print(find_pair(d, 2020))
print(find_triple(d, 2020))

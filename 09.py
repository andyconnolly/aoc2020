d = [int(x) for x in open("09input.txt", "r")]

def find_pair(data, target):
    seen = set()
    for item in data:
        if target - item in seen:
            return True
        seen.add(item)
    return False

def sum_min_max(data):
    min, max = data[0], data[0]
    for val in data:
        if val < min: min = val
        if val > max: max = val
    return min + max

def part1(data, preamble):
    for index in range(preamble, len(data)):
        if not(find_pair(data[index - preamble: index], data[index])):
            return data[index]

def part2(data, value):
    index = data.index(value)
    return [sum_min_max(data[i: j]) 
            for i in range(index) 
            for j in range(i + 1, index) 
            if sum(data[i: j]) == value][0]

print(target := part1(d, 25))
print(part2(d, target))

#test_data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
#print(part1(test_data, 5))
#print(part2(test_data, 127))

#def part2(data, value):
#    index = data.index(value)
#    for i in range(index):
#        sum = data[i]
#        smallest = sum
#        largest = sum
#        if sum < value:
#            for j in range(i + 1, index):
#                sum += data[j]
#                if sum > value:
#                    break
#                if data[j] < smallest: smallest = data[j]
#                if data[j] > largest: largest = data[j]
#                if sum == value:
#                    return (smallest + largest)

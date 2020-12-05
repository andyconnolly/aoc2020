d = {int(x.strip().replace('B','1').replace('F','0').replace('L','0').replace('R','1'), 2) for x in open("05input.txt","r")}

def part1(data):
    max_ID = 0
    for ID in data:
        if max_ID < ID: max_ID = ID
    return max_ID

def part2(data):
    for seat in data:
        if (seat + 1 not in data) and (seat + 2 in data):
            return seat + 1

print(part1(d))
print(part2(d))

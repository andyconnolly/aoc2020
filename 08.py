test_data = ['nop +0','acc +1','jmp +4','acc +3','jmp -3','acc -99','acc +1','jmp -4','acc +6']

d = [x.split() for x in [x.strip() for x in open("08input.txt", "r").readlines()]]

def part1(instructions):
    accumulator = 0
    pos = 0
    executed = set()
    for i in range(len(d)):
        if pos in executed:
            return accumulator, False #finished as we are repeating an instruction
        else:
            executed.add(pos)
            cmd = instructions[pos][0]
            val = int(instructions[pos][1])
            if cmd == 'acc': 
                accumulator += val
            pos += (val if cmd == 'jmp' else 1)
            if pos >= len(d):
                return accumulator, True #Finished correctly

def part2(instructions):
    ops = [(i, 'nop' if x[0] == 'jmp' else 'jmp') for i, x in enumerate(instructions) if x[0] in {'nop', 'jmp'}]
    test = [x[:] for x in instructions]
    for index in ops:
        test[index[0]][0] = index[1]
        result = part1(test)
        if result[1]:
            return result[0], index
        test[index[0]][0] = instructions[index[0]][0] #restore original

print(part1(d)[0])
print(part2(d)[0])

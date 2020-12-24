d = open('18input.txt', 'r').readlines()

import re
from collections import deque

def samePrecedence(data):
    data = deque(data.split())
    result = int(data.popleft())
    while data:
        operator = data.popleft()
        number = int(data.popleft())
        if operator == '+':
            result += number
        else:
            result *= number
    return result

def addBeforeMul(data):
    result = 1
    for x in data.split('*'):
        result *= samePrecedence(x)
    return result

def evaluate(data, fn):
    groups = re.compile(r'(\([^()]+\))').search(data)
    if not groups:
        return fn(data)
    result = fn(groups.group(0).strip('()'))
    return evaluate(data.replace(groups.group(0), str(result)), fn)

def part1(data):
    return sum(evaluate(d, samePrecedence) for d in data)

def part2(data):
    return sum(evaluate(d, addBeforeMul) for d in data)

print(part1(d))
print(part2(d))

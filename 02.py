d = [[[int(z) for z in y[0].split('-')], y[1][0], y[2]] for y in [x.strip().split() for x in open("02input.txt", "r")]]

#each item of d has the form [[num1, num2], char, string]
#for part1: 
#    num1 is the minimum number of occurrences of char in string
#    num2 is the maximum number of occurrences of char in string
#    the string is valid if the number of occurrences of char in string is between min and max 
#for part2: 
#    num1 is the position (index 1-based) of char in string
#    num2 is the position (index 1-based) of char in string
#    the string is valid if either position is char, but not both are char

def part1(data):
    valid = 0
    for [min, max], char, pwd in data:
        cnt = pwd.count(char)
        if cnt >= min and cnt <= max:
            valid = valid + 1
    return valid

def part2(data):
    valid = 0
    for [pos1, pos2], char, pwd in data:
        if (pwd[pos1 - 1] == char or pwd[pos2 - 1] == char) and pwd[pos1 - 1] != pwd[pos2 - 1]:
            valid = valid + 1
    return valid

print(part1(d))
print(part2(d))

#using list comprehensions:
d = [[[int(z) for z in y[0].split('-')], y[1][0], y[2]] for y in [x.strip().split() for x in open("02input.txt", "r")]]
print(len([1 for [min, max], char, pwd in d if (cnt := pwd.count(char)) >= min and cnt <= max]))
print(len([1 for [pos1, pos2], char, pwd in d if (pwd[pos1-1] == char or pwd[pos2-1] == char) and pwd[pos1-1] != pwd[pos2-1]]))

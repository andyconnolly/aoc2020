d = open('22input.txt', 'r').read().strip().split('\n\n')

p1 = [int(x) for x in d[0].split('\n')[1:]]
p2 = [int(x) for x in d[1].split('\n')[1:]]

def getScore(p):
    score = 0
    for i in range(1, len(p) + 1):
        score += i * p[-i]
    return score

def game(p1, p2, recursive):
    states = set()
    while p1 and p2:
        if (state := (tuple(p1), tuple(p2))) in states:
            return True, p1
        states.add(state)
        (c1, *p1), (c2, *p2) = p1, p2
        if recursive and len(p1) >= c1 and len(p2) >= c2:
            p1win = game(p1[:c1], p2[:c2], recursive)[0]
        else:
            p1win = c1 > c2
        if p1win:
            p1.extend((c1, c2))
        else:
            p2.extend((c2, c1))
    return (True, p1) if p1 else (False, p2)

print(getScore(game(p1, p2, False)[1]))
print(getScore(game(p1, p2, True)[1]))
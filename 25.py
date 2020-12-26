d1 = 15113849
d2 = 4206373

def part1(subject_num, card_pk, door_pk):
    PKs = {card_pk, door_pk}
    for i in range(20201227):
        p = pow(subject_num, i, 20201227)
        if p in PKs:
            PKs.remove(p)
            return pow(PKs.pop(), i, 20201227)

print('part 1:', part1(7, d1, d2))
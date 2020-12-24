import re
from itertools import product

class Mem(dict):
    def __setitem__(self, key, value):
        global mask
        x = int(mask.replace("0", "1").replace("X", "0"), 2)
        maskb = int(mask.replace("X", "0"), 2)
        value = (((value | x) ^ x)) | maskb
        super().__setitem__(key, value)

mem = Mem()
with open("14input.txt") as f:
    text = f.read()
    l = ["mask" + x for x in text.split("mask")[1:]]
    l = [re.sub("mask = ([01X]+)", r'mask = "\1"', x) for x in l]

for x in l: exec(x)
print(sum(mem.values()))

class Mem2(dict):
    def __setitem__(self, key, value):
        global mask
        X_pos = [i for i, x in enumerate(mask) if x == "X"]
        X_bin = [2 ** (len(mask) - 1 - x) for x in X_pos]
        X_mask = sum(X_bin)
        maskb = int(mask.replace("X", "0"), 2)
        key |= maskb
        key |= X_mask
        key ^= X_mask
        for digits in product(*(range(2) for _ in range(len(X_pos)))):
            super().__setitem__(key + sum(x * y for x, y in zip(X_bin, digits)), value)

mem = Mem2()
for x in l: exec(x)
print(sum(mem.values()))

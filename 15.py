data = "13,16,0,12,15,1"

def getNext(data, end):
    seq = {int(x):index for index, x in enumerate(data.split(','), start = 1)}
    spoken = 0
    for n in range(len(seq) + 1, end):
        if spoken in seq:
            next_num = n - seq[spoken]
            seq[spoken] = n
            spoken = next_num
        else:
            seq[spoken] = n
            spoken = 0
    return spoken

print(getNext(data, 2020))
print(getNext(data, 30000000))

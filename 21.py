a=[x[:-1].split(' (contains ') for x in open('21input.txt', 'r').read().split('\n')[:-1]]
A={}
allingredients=set()
for x in a:
    for allergene in x[1].split(', '):
        ingr = set(n for n in x[0].split(' '))
        allingredients = allingredients | ingr
        if not allergene in A.keys():
            A[allergene] = ingr
        else:
            A[allergene] = ingr.intersection(A[allergene])

#reducing to ingredients without allergene
for i in A.values():
    allingredients-=i

ct=0
for x in a:
    for i in allingredients:
        if i in x[0].split(' '): ct+=1

for x in A:
    A[x]=A[x]-allingredients

reducing=True
solved={}
while reducing:
    reducing = False
    for x in A:
        if len(A[x])==1 and not x in solved:
            reducing = True
            print('solved', x)
            cur=x
            solved[x]=A[x].pop()
            del A[x]
            break
    for x in A:
        A[x]-={solved[cur]}
    print(solved)

allergene_sorted = sorted(solved.keys())
out = ''
for x in allergene_sorted:
    out += solved[x] + ','

print(allergene_sorted)
print(ct)
print(out[:-1])
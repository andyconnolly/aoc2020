d = [int(x) for x in open("10input.txt", "r")]

adapters = [0] + sorted(d[:])
adapters.append(adapters[-1] + 3)
diffs = [adapters[i + 1] - adapters[i] for i in range(len(adapters)-1)]
print("Part 1:", diffs.count(1) * diffs.count(3))

routes = dict()
routes[0] = 1
for i in adapters[1:]:
    routes[i] = routes.get(i - 1, 0) + routes.get(i - 2, 0) + routes.get(i - 3, 0)

print("Part 2: ", routes[adapters[-1]])

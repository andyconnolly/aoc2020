import re

raw_rules, your_ticket, nearby_tickets = open('16input.txt','r').read().strip().split('\n\n')
regexp = re.compile(r'([^:]+): (\d+)-(\d+) or (\d+)-(\d+)')
rules = []

for line in raw_rules.splitlines():
    field, lo1, hi1, lo2, hi2 = regexp.fullmatch(line).groups()
    rules.append((field, int(lo1), int(hi1), int(lo2), int(hi2)))

error_rate = 0
no_of_rules = len(rules)
cols = [set(range(no_of_rules)) for x in range(no_of_rules)]

for ticket in nearby_tickets.splitlines()[1:]:
    ticket_rules = []
    for num in [int(x) for x in ticket.split(',')]:
        matches = set(i for i, (x, lo1, hi1, lo2, hi2) in enumerate(rules) if lo1 <= num <= hi1 or lo2 <= num <= hi2)
        if len(matches) == 0:
            error_rate += num
            break
        ticket_rules.append(matches)
    else:
        for i in range(no_of_rules):
            cols[i] = cols[i].intersection(ticket_rules[i])

print(error_rate)

total = 1
singles = set()
your_ticket = [int(number) for number in your_ticket.splitlines()[1].split(",")]
while len(singles) != no_of_rules:
    for i, col in enumerate(cols):
        if len(col) > 1:
            col -= singles
        elif len(col) == 1:
            singles = singles.union(col)
            if rules[col.pop()][0].startswith("departure"):
                total *= your_ticket[i]

print(total)

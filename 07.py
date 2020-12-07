import re
bags = {re.match('^\w+ \w+', line).group(0): 
                 {x[1]: int(x[0]) for x in re.findall('(\d+) ([\w\s?]+) ', line)} 
                 for line in open('07input.txt', 'r')}

def get_ancestors(colour):
    colours = {parent for parent, children in bags.items() if colour in children}
    if colours:
        for col in colours:
            colours = colours.union(get_ancestors(col))
    return colours

def get_descendents(colour):
    total = 1
    for col, amount in bags[colour].items():
        total += (amount * get_descendents(col))
    return total

colour = 'shiny gold'
print(len(get_ancestors(colour)))
print(get_descendents(colour) - 1) #don't include the holding bag

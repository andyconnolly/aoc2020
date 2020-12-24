import re

def import_data():
    groups = open('19input.txt', 'r').read().split('\n\n')
    rules = create_rules(groups[0].split('\n'))
    messages = groups[1].split('\n')
    return rules, messages

def create_rules(rules_data):
    rules = dict()
    for line in rules_data:
        key, line = line.split(': ')
        groups = [[x.replace('"', '') for x in group] for group in [x.split() for x in line.split(' | ')]]
        groups = [[int(x) if x.isnumeric() else x for x in group] for group in groups]
        rules[int(key)] = groups
    return rules

def rule_has_only_strings(rule):
    return all([isinstance(c, str) for group in rule for c in group])

def find_rule_with_only_strings(rules):
    for key, rule in rules.items():
        if rule_has_only_strings(rule):
            return key
    return None

def replace_refs_in_rule(rules, search_key, replacement):
    for key, rule in rules.items():
        for i, group in enumerate(rule):
            for j, c in enumerate(group):
                if c == search_key:
                    rules[key][i][j] = replacement
    return rules

def convert_rules_to_regex(rules):
    while True:
        found_key = find_rule_with_only_strings(rules)
        if not found_key:
            break 
        found_rule = rules.pop(found_key)
        regex = convert_rule_to_regex(found_rule)	
        rules = replace_refs_in_rule(rules, found_key, regex)
    return rules

def convert_rule_to_regex(rule):
    return r'(' + '|'.join(['(' + ''.join([c for cs in group for c in cs]) + ')' for group in rule]) + ')'	

def count_valid_messages_by_regex(messages, regex):
    regex += r'$' # Include line-end in regex to match whole line
    p = re.compile(regex)
    count = 0
    for message in messages:
        match = p.match(message)
        if match: 
            count += 1
    return count

# Part 1
rules, messages = import_data()
rules = convert_rules_to_regex(rules)
regex = convert_rule_to_regex(rules[0])
print('Answer 1:', count_valid_messages_by_regex(messages, regex))

# Part 2
rules, messages = import_data()

# Update rules
rules[8]  = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

rules = convert_rules_to_regex(rules)

regex42 = rules[8][0][0]
regex31 = rules[11][0][1]
regex8  = regex42 + '+'
regex11 = r'(' + '|'.join([f'{regex42}{{{n}}}{regex31}{{{n}}}' for n in range(1, 5)]) + ')'
regex0  = regex8 + regex11

print('Answer 2:', count_valid_messages_by_regex(messages, regex0))
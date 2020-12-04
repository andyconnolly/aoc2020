test_data = [
'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
'byr:1937 iyr:2017 cid:147 hgt:183cm',
'',
'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
'hcl:#cfa07d byr:1929',
'',
'hcl:#ae17e1 iyr:2013',
'eyr:2024',
'ecl:brn pid:760753108 byr:1931',
'hgt:179cm',
'',
'hcl:#cfa07d eyr:2025 pid:166559648',
'iyr:2011 ecl:brn hgt:59in']

test_valid = [
'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
'hcl:#623a2f',
'',
'eyr:2029 ecl:blu cid:129 byr:1989',
'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
'',
'hcl:#888785',
'hgt:164cm byr:2001 iyr:2015 cid:88',
'pid:545766238 ecl:hzl',
'eyr:2022',
'',
'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719']

data = [x.strip() for x in open("04input.txt", "r")]

class PassportOriginal:
    def __init__(self):
        self.byr = '' # (Birth Year)
        self.iyr = '' # (Issue Year)
        self.eyr = '' # (Expiration Year)
        self.hgt = '' # (Height)
        self.hcl = '' # (Hair Color)
        self.ecl = '' # (Eye Color)
        self.pid = '' # (Passport ID)
        self.cid = '' #(Country ID)
    
    def add(self, field, value):
        if field == 'byr':   self.byr = value
        elif field == 'iyr': self.iyr = value
        elif field == 'eyr': self.eyr = value
        elif field == 'hgt': self.hgt = value
        elif field == 'hcl': self.hcl = value
        elif field == 'ecl': self.ecl = value
        elif field == 'pid': self.pid = value
        elif field == 'cid': self.cid = value
    
    def get(self, field):
        if field == 'byr':   return self.byr
        elif field == 'iyr': return self.iyr
        elif field == 'eyr': return self.eyr
        elif field == 'hgt': return self.hgt
        elif field == 'hcl': return self.hcl
        elif field == 'ecl': return self.ecl
        elif field == 'pid': return self.pid
        elif field == 'cid': return self.cid
    
    def is_valid_part1(self):
        return self.byr != '' and self.iyr != '' and self.eyr != '' and self.hgt != '' and self.hcl != '' and self.ecl != '' and self.pid != ''
    
    def is_valid_part2(self):
        if len(self.byr) == 4 and (y := int(self.byr)) >= 1920 and y <= 2002:
            if len(self.iyr) == 4 and (y := int(self.iyr)) >= 2010 and y <= 2020:
                if len(self.eyr) == 4 and (y := int(self.eyr)) >= 2020 and y <= 2030:
                    if len(self.hgt) > 3 and ((self.hgt.endswith('cm') and (h := int(self.hgt[:-2])) >= 150 and h <= 193) 
                                             or (self.hgt.endswith('in') and (h := int(self.hgt[:-2])) >= 59 and h <= 76)):
                        if len(self.hcl) == 7 and self.hcl[0] == '#' and is_num(self.hcl[1:], 16):
                            if len(self.ecl) == 3 and self.ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                                if len(self.pid) == 9 and is_num(self.pid, 10):
                                    return True
        return False

class Passport:
    def __init__(self):
        self.fields = dict()
        self.fields['byr'] = '' # (Birth Year)
        self.fields['iyr'] = '' # (Issue Year)
        self.fields['eyr'] = '' # (Expiration Year)
        self.fields['hgt'] = '' # (Height)
        self.fields['hcl'] = '' # (Hair Color)
        self.fields['ecl'] = '' # (Eye Color)
        self.fields['pid'] = '' # (Passport ID)
        self.fields['cid'] = '' #(Country ID)
    
    def __str__(self):
        return str(self.fields)
    
    def __repr__(self):
        return str(self.fields)
    
    def add(self, field, value):
        self.fields[field] = value
    
    def get(self, field):
        return self.fields[field]
    
    def is_valid_part1(self):
        return self.fields['byr'] != '' and self.fields['iyr'] != '' and self.fields['eyr'] != '' and self.fields['hgt'] != '' and self.fields['hcl'] != '' and self.fields['ecl'] != '' and self.fields['pid'] != ''
    
    def is_valid_part2(self):
        byr = self.fields['byr']
        iyr = self.fields['iyr']
        eyr = self.fields['eyr']
        hgt = self.fields['hgt']
        hcl = self.fields['hcl']
        ecl = self.fields['ecl']
        pid = self.fields['pid']
        cid = self.fields['cid']
        if len(byr) == 4 and (y := int(byr)) >= 1920 and y <= 2002:
            if len(iyr) == 4 and (y := int(iyr)) >= 2010 and y <= 2020:
                if len(eyr) == 4 and (y := int(eyr)) >= 2020 and y <= 2030:
                    if len(hgt) > 3 and ((hgt.endswith('cm') and (h := int(hgt[:-2])) >= 150 and h <= 193) 
                                             or (hgt.endswith('in') and (h := int(hgt[:-2])) >= 59 and h <= 76)):
                        if len(hcl) == 7 and hcl[0] == '#' and is_num(hcl[1:], 16):
                            if len(ecl) == 3 and ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                                if len(pid) == 9 and is_num(pid, 10):
                                    return True
        return False

def is_num(value, base):
    try:
        x = int(value, base)
        return True
    except:
        return False

def get_passports(data):
    passports = list()
    details = Passport()
    for line in data:
        if line.strip() == '':
            passports.append(details)
            details = Passport()
        else:
            items = line.strip().split()
            for item in items:
                field, value = item.split(':')
                details.add(field, value)
    if line.strip() != '':
        passports.append(details)
    return passports

def count_valid(passports, part):
    count = 0
    if part == 1:
        for passport in passports:
            if passport.is_valid_part1():
                count +=1
    elif part == 2:
        for passport in passports:
            if passport.is_valid_part2():
                count +=1
    return count

print(count_valid(get_passports(data), 1))
print(count_valid(get_passports(data), 2))

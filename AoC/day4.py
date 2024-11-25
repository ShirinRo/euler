import re

day4Input = open('4input', 'r')
passports = day4Input.readlines()

def isValidPassport(passport: dict):
    if set(passport.keys()) == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}:
        return True
    elif set(passport.keys()) == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
        return True
    return False


def addKeysInLineToDictionary(line: str, dictionary: dict):
    ind = line.find("byr:")
    if ind != -1:
        birthYear = line[ind+4:].split()[0]
        if 1920 <= int(birthYear) <= 2002:
            dictionary["byr"] = line[ind+4:].split()[0]

    ind = line.find("iyr:")
    if ind != -1:
        issueYear = line[ind+4:].split()[0]
        if 2010 <= int(issueYear) <= 2020:
            dictionary["iyr"] = line[ind+4:].split()[0]

    ind = line.find("eyr:")
    if ind != -1:
        expirationYear = line[ind + 4:].split()[0]
        if 2020 <= int(expirationYear) <= 2030:
            dictionary["eyr"] = expirationYear

    ind = line.find("hgt:")
    if ind != -1:
        height = line[ind+4:].split()[0]
        match = re.fullmatch(r"([0-9]+)(cm|in)", height)
        if match is not None:
            measure = match.group(1)
            unit = match.group(2)
            if unit == "cm" and 150 <= int(measure) <= 193:
                dictionary["hgt"] = height
            if unit == "in" and 59 <= int(measure) <= 76:
                dictionary["hgt"] = height

    ind = line.find("hcl:")
    if ind != -1:
        hairColor = line[ind+4:].split()[0]
        if re.fullmatch(r"#([0-9]|[a-f]){6}", hairColor) is not None:
            dictionary["hcl"] = hairColor

    ind = line.find("ecl:")
    if ind != -1:
        eyeColor = line[ind+4:].split()[0]
        validColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if eyeColor in validColors:
            dictionary["ecl"] = eyeColor

    ind = line.find("pid:")
    if ind != -1:
        passportID = line[ind+4:].split()[0]
        if re.fullmatch(r"[0-9]{9}", passportID) is not None:
            dictionary["pid"] = passportID

    ind = line.find("cid:")
    if ind != -1:
        dictionary["cid"] = line[ind+4:].split()[0]


countValid = 0
minimum = 0
maximum = 100
line: str
currPassport = dict()
for line in passports:
    if line == "\n":
        print(currPassport)
        if isValidPassport(currPassport):
            print("Valid!")
            countValid += 1
        else:
            print("Invalid! :(")
        currPassport = dict()
    else:
        addKeysInLineToDictionary(line, currPassport)
        # print(currPassport)
    # match = re.match(r"([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)", line)

print(countValid)
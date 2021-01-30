import re

fields_clear = {"byr" : None, "iyr" : None, "eyr" : None, "hgt": None, "hcl": None, "ecl": None, "pid": None, "cid": None}
fields_checker = {    \
    "byr": "^(?:(?:19[2-9][0-9])|(?:200[0-2]))$", \
    "iyr": "^20(?:(?:1[0-9])|(?:20))$", \
    "eyr": "^20(?:(?:2[0-9])|(?:30))$", \
    "hgt": "^(?:(?:(?:(?:1[5-8][0-9])|(?:19[0-3]))cm)|(?:(?:(?:59)|(?:6[0-9])|(?:7[0-6]))in))$", \
    "hcl": "^#([0-9]|[a-f]){6}$", \
    "ecl": "^(amb|blu|brn|gry|grn|hzl|oth)$", \
    "pid": "^\d{9}$", \
    }

def passport_valid(fields):
    for key in fields.keys():
        if key == "cid":
            continue

        if not fields[key]:
            return False, 1, key
        
        value = fields[key]
        if not re.match(fields_checker[key], value):
            return False, 2, key       

    return True, 0, None


valid_passes = 0

with open("challenge_4_data") as f:

    fields = fields_clear.copy()
    s = ""
    num = 0
    for line in f:
        s = s + line
        if not line.strip():


            pass_valid, invalid_cause, key_cause = passport_valid(fields)
            
            if pass_valid:
                valid_passes = valid_passes+1
            elif invalid_cause == 2:
                 print( "++++++++++++++++ {} - Failure: {} +++++++++++++++".format(num, key_cause))
                 print (fields)
                 print (passport_valid(fields))
                 print(s)

            fields = fields_clear.copy()
            num = num + 1
            s = ""
            continue

        for field in line.split(" "):
            key = field.split(":")[0]
            value = field.split(":")[1].strip()
            fields[key] = value

    if passport_valid(fields):
        valid_passes = valid_passes+1

print("Valid passes: {}".format(valid_passes))
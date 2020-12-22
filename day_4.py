
# Detect which passports have all required fields

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

opt_fields = ["cid"]

sample_batch = [{"ecl":"gry",
"pid":"860033327", "eyr":2020, "hcl":"#fffffd",
"byr":1937, "iyr":2017, "cid":147, "hgt":"183cm"},
{"iyr":2013, "ecl":"amb", "cid":350, "eyr":2023, "pid":"028048884",
"hcl":"#cfa07d", "byr":1929},
{"hcl":"#ae17e1", "iyr":2013,
"eyr":2024,
"ecl":"brn", "pid":"760753108", "byr":1931,
"hgt":"179cm"},
{"hcl":"#cfa07d", "eyr":2025, "pid":"166559648",
"iyr":2011, "ecl":"brn", "hgt":"59in"}
]

batch_raw = []

with open("day_4_data.txt", "r", encoding="utf-8") as f:
    for line in f:
        batch_raw.append(line.split())

for i, item in enumerate(batch_raw):
    if item == []:
        batch_raw[i] = ["new entry"]

batch = []
one_diction = {}

for items in batch_raw:
    if items == ['new entry']:
        batch.append(one_diction)
        one_diction = {}
    else:
        for one_item in items:
            key, value = one_item.split(":")
            one_diction[key] = value

def value_count_check(lst):
    '''
    Count the number of passports that have required fields

    Input, list of dictionaries: list of dictionaries that represent
    passport key and value pairs

    Output, integer: count of valid dictionaries
    '''
    count_pass = 0

    for dictionary in lst:
        count_fields = 0
        for field in req_fields:
            if field in dictionary.keys():
                count_fields += 1
            
        if count_fields == len(req_fields):
            count_pass += 1
    
    return count_pass

def value_check(lst):
    '''
    Check the values of selected required fields

    Input, list of dictionaries: list of dictionaries that represent
    passport key and value pairs

    Output, integer: count of valid dictionaries based on parameters
    '''
    count_pass = 0

    for dictionary in lst:
            # check that passport has required fields first
        count_fields = 0
        for field in req_fields:
            if field in dictionary.keys():


        for key, value in dictionary.items():
            valid = True
            while valid == True:
                if key == "byr":
                    if (value < 1920 and value > 2002) or len(str(value)) != 4:
                        valid = False
                if key == "iyr":
                    if (value < 2010 and value > 2020) or len(str(value)) != 4:
                        valid = False
                if key == "eyr":
                    if (value < 2020 and value > 2030) or len(str(value)) != 4:
                        valid = False
                if key == "hgt":
                    if value[-2:] == "cm":
                        if int(value[:-2]) < 150 and int(value[:-2]) > 193:
                            valid = False
                    elif value[-2:] == "in":
                        if int(value[:-2]) < 59 and int(value[:-2]) > 76:
                            valid = False
                    else:
                        valid = False
                if key == "hcl":
                    if value[0] != "#" or len(value) != 6 or not set(value).isdisjoint(set("ghijklmnopqrstuvwxyz")):
                        valid = False
                if key == "ecl":
                    if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        valid = False
                if key == "pid":
                    if len(value) != 9:
                        valid = False
                
                break 

            if valid == True:
                count_pass += 1

    return count_pass

                



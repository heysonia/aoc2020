import sys
import re

def year_check(number, low, high):
    state = False
    if len(number) == 4:
        if (int(number) <= high) & (int(number) >= low):
            state = True
    return state

def height_check(height):
    state = False
    if height[-2:] == 'cm':
        hcm = int(height[:-2])
        if (hcm >= 150) & (hcm <=193):
            state = True
    if height[-2:] == 'in':
        hic = int(height[:-2])
        if (hic >= 59) & (hic <= 76):
            state = True
    return state

def hair_check(hair_colour):
    state = False
    def special_match(strg, search=re.compile(r'[^a-f0-9.]').search): # [] indicate capture group, ^ indicates 'NOT', . is literal i.e. not case sensitive
        return not bool(search(strg)) # regex returns null if finds nothing - i.e. bool is False, match object if yes bool is True
    # not False is True -> all if within the criteria, not True is False -> finds something not matching criteria
    if (hair_colour[0] == '#') & (len(hair_colour[1:]) == 6):
        state = special_match(hair_colour[1:])
    return state

def passport_validator(list_of_passports):
    need_these = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    good_to_have = ['cid']
    cnt = 0
    for psp in list_of_passports:
        psp_clean = psp.replace('\n', ' ').replace(' ', ' ')
        psp_keys = [kv.split(':')[0] for kv in psp_clean.strip(' ').split(' ')]
        psp_values = [kv.split(':')[1] for kv in psp_clean.strip(' ').split(' ')]
        psp_dict = dict(zip(psp_keys, psp_values))
        psp_dict = dict(sorted(psp_dict.items()))
        try:
            del psp_dict['cid']
        except KeyError:
            pass # this makes sure the loop continues processing, continue will jump back to top of the loop

        if set(need_these).issubset(psp_keys):
            # SORRY THIS IS SO UGLY, had to debug as i didn't read the instructions carefully the first time :(
            if (year_check(psp_dict['byr'], 1920, 2002)) & \
                            (year_check(psp_dict['iyr'], 2010, 2020)) & \
                                (year_check(psp_dict['eyr'], 2020, 2030)):
                state = 'years_passed'
            else:
                # print(f'issue with years {psp_dict}')
                continue

            if height_check(psp_dict['hgt']):
                state = 'height_passed'
            else:
                # print(f'issue with hgt {psp_dict}')
                continue

            if hair_check(psp_dict['hcl']):
                state = 'hcl_passed'
            else:
                # print(f'issue with hcl {psp_dict}')
                continue

            if psp_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                state = 'ecl_passed'
            else:
                # print(f'issue with ecl {psp_dict}')
                continue

            if (psp_dict['pid'].isdigit()) & (len(psp_dict['pid']) == 9):
                state = 'pid_passed'
            else:
                # print(f'issue with PID {psp_dict}')
                continue
            # print(f'SUCCESS {psp_dict}')
            cnt += 1
        else:
            # print(f'Missing keys in {psp_dict}')
            continue
    return cnt

if __name__ == '__main__':

    data_loc = sys.argv[1]
    with open(data_loc) as f:
        passport_list = f.read().strip("/n").split("\n\n")
        # print(f'num of passports: {len(passport_list)}')
    print(passport_validator(passport_list))

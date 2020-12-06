import sys

def password_checker(list_of_pwd):
    low_criteria = []
    high_criteria = []
    letter_criteria = []
    password = []
    for pwd in list_of_pwd:
        num_let_pwd = pwd.split(' ')
        password.append(num_let_pwd[-1])
        letter_criteria.append(num_let_pwd[1][0])
        low_criteria.append(num_let_pwd[0].split('-')[0])
        high_criteria.append(num_let_pwd[0].split('-')[1])
        assert len(low_criteria) == len(high_criteria) == len(letter_criteria) == len(password)

    valid_cnt = 0

    for l,h,let,pwd in zip(low_criteria, high_criteria, letter_criteria, password):
        if let in pwd:
            cnt = pwd.count(let)
            if (cnt>=int(l)) & (cnt <=int(h)):
                valid_cnt += 1
        else:
            print('password not valid')
            continue

    return valid_cnt

def password_checker2(list_of_pwd):
    first_criteria = []
    second_criteria = []
    letter_criteria = []
    password = []
    for pwd in list_of_pwd:
        num_let_pwd = pwd.split(' ')
        password.append(num_let_pwd[-1])
        letter_criteria.append(num_let_pwd[1][0])
        first_criteria.append(num_let_pwd[0].split('-')[0])
        second_criteria.append(num_let_pwd[0].split('-')[1])
        assert len(first_criteria) == len(second_criteria) == len(letter_criteria) == len(password)

    valid_cnt = 0

    for l,h,let,pwd in zip(first_criteria, second_criteria, letter_criteria, password):
        if let in pwd:
            first = int(l) - 1
            second = int(h) - 1
            if (pwd[first] == let) is not (pwd[second] == let):
                valid_cnt += 1
        else:
            print('password not valid')
            continue

    return valid_cnt

if __name__ == '__main__':
    data_loc = sys.argv[1]

    with open(data_loc) as f:
        passwords_list = f.read().splitlines()
#     print(password_checker(passwords_list))

    print(password_checker2(passwords_list))



# a = password_checker(["1-3 a: abcde", "2-9 c: ccccccccc", "1-3 b: cdefg"])
# print(a)

# a = password_checker2(["1-3 a: abcde", "2-9 c: ccccccccc", "1-3 b: cdefg"])
# print(a)
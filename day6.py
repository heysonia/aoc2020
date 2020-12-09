import sys
from collections import Counter

def count_unique(string):
    return len(set(string.replace('\n', '')))

def count_all_yes(string):
    group_yes = 0
    answers_in_group = string.split('\n')
    num_people_in_group = len(answers_in_group)
    group_count = Counter(string.replace('\n', ''))
    for yes in group_count.values():
        if yes == num_people_in_group:
            group_yes += 1
    return group_yes

def sum_counts(list_of_strings, count_type):
    return sum([count_type(group) for group in list_of_strings])

if __name__ == '__main__':

    data_loc = sys.argv[1]
    with open(data_loc) as f:
        answers = f.read().split("\n\n")
    # print(sum_counts(answers, count_unique)) # PART 1
    print(sum_counts(answers,count_all_yes))  # PART 2
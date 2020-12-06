# import argparse
import sys
import logging
from itertools import combinations
import numpy as np

logger = logging.getLogger()
logger.setLevel(logging.INFO)


logger.addHandler(logging.StreamHandler(sys.stdout))

def two_2020_numbers(expense_report):
    """
    Finds two numbers where sum is 2020 and multiplies these two numbers together
    :param list expense_report: list of integers
    :return: multiplication of two numbers which add up to 2020
    """
    # if number is > 2020 ignore and sort ascending
    clean_list = sorted(x for x in expense_report if x < 2020)
    # add the first to the last, if < 2020 move to next smallest one until >2020 then save this as the offset to
    # look from the first number from then shift big number down until < 2020 then repeat next smallest
    len_list = len(clean_list)
    offset = 0
    final_number = 0
    for i in range(len_list):
        big_num = clean_list[len_list-(i+1)]
        if offset >= len_list-1:
            logging.debug('All numbers are too small to add up to 2020')
            break
        else:
            small_num = clean_list[offset]
            logging.info('Trying %i and %i' %(small_num, big_num))

        while (small_num + big_num) < 2020:
            offset += 1
            if offset >= len_list-1: # if goes beyond list exit while loop
                logging.info('Smaller number %i is too small' %small_num)
                break
            small_num = clean_list[offset]

        if (small_num + big_num) == 2020:
            # if we find the two numbers then continue
            logging.info('Found the two numbers!')
            final_number = small_num * big_num
            break

    return final_number

def n_2020_numbers(expense_report, num_digits = 3):
    # if number is > 2020 ignore and sort ascending
    clean_list = sorted(x for x in expense_report if x < 2020)
    list_combination = [comb for comb in combinations(clean_list, num_digits) if sum(comb) == 2020]
    return np.prod(list_combination[0])


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("list of expenses")
    #
    # args = parser.parse_args()
    expenses_txt_loc = sys.argv[1]
    num_digits = sys.argv[2]

    with open(expenses_txt_loc) as f:
        expenses_str = f.read().splitlines()
    expenses_int = [int(x) for x in expenses_str]
    if num_digits == 2:
        print(two_2020_numbers(expenses_int))
    else:
        print(n_2020_numbers(expenses_int))
    # print(expenses_int)

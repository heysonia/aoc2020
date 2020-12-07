import sys
import math
import numpy as np

def row_col_finder(start, end, char):
    """

    :param start: starting row
    :param end: ending row
    :param char: front or back half of plane, left or right of plane
    :return:
    """
    split = (end-start)/2
    if char in ('F', 'L'):
        # keep lower half
        s = start
        e = math.floor(start + split)
    if char in ('B', 'R'):
        # keep upper half
        s = math.ceil(start + split)
        e = end
    return s, e

def highest_seat_finder(seat_chars):
    """

    :param seat_chars:
    :return: Part 1: return highest seat, Part 2: return list of seat ID not in first or last row
    """

    rows = []
    seat_ids = []
    # highest_seat = 0

    for seat in seat_chars:
        row_chars = seat [:-3]
        col_chars = seat[-3:]
        r_s = 0
        r_e = 127
        c_s = 0
        c_e = 7
        for r in list(row_chars):
            r_s, r_e = row_col_finder(r_s, r_e, r)
        for c in list(col_chars):
            c_s, c_e = row_col_finder(c_s, c_e, c)

        assert r_s == r_e, 'Row Finder not complete'
        assert c_s == c_e, 'Column Finder not complete'

        seat_id = (r_s * 8) + c_s

        # Part 1
        # if seat_id > highest_seat:
        #     highest_seat = seat_id

        # Part 2
        if r_s > 0 and r_s < 127:
            seat_ids.append(seat_id)
    return seat_ids

def seat_finder(occupied_seats):
    ordered_seats = sorted(occupied_seats)
    diff_seats = list(np.diff(ordered_seats))
    # seat missing in between the diff = 2 (i.e. seat where next seat is two after) and the seat after (i.e. missing + 1)
    return ordered_seats[diff_seats.index(2)] + 1

if __name__ == '__main__':

    data_loc = sys.argv[1]
    with open(data_loc) as f:
        seat_chars = f.read().splitlines()
    print(seat_finder(highest_seat_finder(seat_chars)))
import sys
import math

def expand_grid(slope_pattern, R, D):
    """
    returns full repeated pattern for entire mountain
    :param list slope_pattern: list of a string of '#' and '.' characters where '#' denotes a tree
    :param int R: number to traverse right

    :return:
    """
    len_patterns = len(slope_pattern)
    steps_down_to_end = math.ceil(len_patterns/D) - 1 # ignore first row
    len_needed_last_slope = steps_down_to_end * R + 1 # add extra step as starts at (0,1)

    def expand_str(s, len_s):
        return (s * math.ceil(len_s / len(s)))[:len_s]

    slopes = [expand_str(s, len_needed_last_slope) for s in slope_pattern]

    return slopes

def count_trees(slopes, R, D):
    """
    Traverses down list of slopes according to R and D
    :param list slopes: list of a full "mountain" of repeated strings of '#' and '.' characters where '#' denotes a tree
    :param int R: number to traverse right
    :param int D: number to traverse down
    :return int tree_cnt: number of trees found after traversing down slopes
    """
    tree_cnt = 0
    r_pos = 0
    d_pos = 0

    for slope_num, slope in enumerate(slopes):
        if r_pos >= len(slope):
            break
        if slope_num == d_pos:
            # if we are on the slope level with D down (i.e. 0, 2, 4... for D = 2)
            if slope[r_pos] == '#':
                tree_cnt += 1
            d_pos += D
            r_pos += R
    return tree_cnt

if __name__ == '__main__':
    data_loc = sys.argv[1]

    with open(data_loc) as f:
        slope_patt = f.read().splitlines()

    # R = int(sys.argv[2])
    # D = int(sys.argv[3])
    # print('Count Trees:', count_trees(expand_grid(slope_patt, R, D), R, D))
    t1 = count_trees(expand_grid(slope_patt, 1, 1), 1, 1)
    t2 = count_trees(expand_grid(slope_patt, 3, 1), 3, 1)
    t3 = count_trees(expand_grid(slope_patt, 5, 1), 5, 1)
    t4 = count_trees(expand_grid(slope_patt, 7, 1), 7, 1)
    t5 = count_trees(expand_grid(slope_patt, 1, 2), 1, 2)
    print(t1, t2, t3, t4, t5)
    print(f'mult_trees {t1 * t2* t3 * t4 * t5}')
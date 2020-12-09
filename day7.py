import sys

def split_rules(rule):
    split_rule = rule.split('contain')
    main_bag = split_rule[0][:-6].strip(' ')  # remove word 'bags' tailing at end
    bag_components = split_rule[1].strip(' ')
    return main_bag, bag_components

def num_bags_to_choose(colour, list_rules):
    # which main bags can contain colour of desired bag - "shiny gold" in Part 1
    outer_bags = [] # get list of bags to check if other bags in it
    outer = True # condition to keep looking for sub bags

    for rule in list_rules:
        bag, parts = split_rules(rule)
        if colour in parts:
            outer_bags.append(bag)

    all_legit_bags = outer_bags # keep a list of all the bags found so far

    while outer:
        if len(outer_bags) == 0: # if there are no more outer bags to be found
            break
        else:
            inner_bags = outer_bags # trying to find bags where the outer bag is inside another bag
            all_legit_bags = all_legit_bags + outer_bags # keep adding to the list of bags where we can find the color in
            outer_bags = [] # which outer bags have these inner bags
            for b in inner_bags:
                for rule in list_rules:
                    bag, parts = split_rules(rule)
                    if b in parts:
                        outer_bags.append(bag)

    return len(set(all_legit_bags))

def num_bags_within(color, list_rules):
    count = 0 # initialise count of bags
    inner = True
    inside_bag_rules = [] # rules inside

    for rule in list_rules:
        bag, parts = split_rules(rule)
        if color in bag:
            parts = parts.replace('bags', '').replace('bag', '').strip('.').strip(' ') # bags before bag
            if 'no other' in parts:
                continue
            inside_bag_rules = parts.split(', ')

    inside_bags = {} # dict of bag and counts
    for bag in inside_bag_rules:
        inside_bags[bag[2:].strip(' ')] = int(bag[0])

    while inner:
        if len(inside_bags) == 0:
            break
        else:
            look_for_bags = inside_bags.keys()  # look for which bags
            how_many_bags = inside_bags.values() # how many of these bags
            count += sum(inside_bags.values())  # add all the bag counts
            print(inside_bags)
            inside_bags = {}  # reset inside bag dictionary
            for b, v in zip(look_for_bags, how_many_bags):
                inside_bag_rules = []
                # print(f'looking at {b}')
                for rule in list_rules:
                    bag, parts = split_rules(rule)
                    if b in bag:
                        parts = parts.replace('bags', '').replace('bag', '').strip('.').strip(' ')
                        if 'no other' in parts:
                            continue
                        inside_bag_rules = parts.split(', ')
                for bag in inside_bag_rules:
                    try:
                        inside_bags[bag[2:].strip(' ')] += int(bag[0]) * v
                    except KeyError:
                        inside_bags[bag[2:].strip(' ')] = int(bag[0]) * v #multiply top level
    return count

if __name__ == '__main__':

    data_loc = sys.argv[1]
    bag_colour = sys.argv[2]
    with open(data_loc) as f:
        bag_rules = f.read().splitlines()

    # print(num_bags_to_choose(bag_colour, bag_rules)) # PART 1
    print(num_bags_within(bag_colour, bag_rules))
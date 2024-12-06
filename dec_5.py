
def main():

    with open("input_dec_5.txt", "r") as infile:
        lines = infile.readlines()
    order_items, options = parse_indata(lines)
    valid_list = check_options(options, order_items)
    total = 0
    for val in valid_list:
        mid_id = len(val)//2
        total += val[mid_id]
    print(f"main total {total}")

def parse_indata(lines):
    order_items = []
    options = []
    for line in lines:
        if "|" in line:
            a,b = line.strip('\n').split("|")
            a,b = int(a),int(b)
            order_items += [(a,b)]
        if "," in line:
            option = []
            parts = line.strip("\n").split(",")
            for part in parts:
                option += [int(part)]
            options += [option]
    return order_items, options

def check_options(options, rules):
    valid_list = []
    for possible_option in options:
        if check_option(possible_option, rules):
            valid_list += [possible_option]
    return valid_list

def test_first():
    test_data='''\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''
    lines = test_data.split("\n")
    rules, options = parse_indata(lines)
    print(rules)
    print(options)
    valid = check_options(options, rules)
    print(valid)
    total = 0
    for val in valid:
        mid_id = len(val)//2
        total += val[mid_id]
    print(total)


def test_second():
    test_data='''\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''
    lines = test_data.split("\n")
    rules, options = parse_indata(lines)
    valid = check_options(options, rules)
    invalid = [i for i in options if i not in valid]
    print(invalid)
    invalid = order_invalid(invalid, rules)
    total = 0
    for val in invalid:
        mid_id = len(val)//2
        total += val[mid_id]
    print(total)

def order_invalid(invalid_list, rules):
    ordered_list = []
    import random
    for invalid in invalid_list:
        ordered_item = []
        for item_index, item in enumerate(invalid):
            if len(ordered_item) == 0:
                # insert first
                ordered_item += [item]
            else:
                min_index = 0
                max_index = len(ordered_item)
                for rule in rules:
                    if item in rule:
                        if item == rule[0]:
                            if rule[1] in ordered_item:
                                # item should be prepended to the found item
                                rule_item_index = ordered_item.index(rule[1])
                                max_index = rule_item_index if rule_item_index < max_index else max_index
                        else:
                            if rule[0] in ordered_item:
                                # item should be after item
                                rule_item_index = ordered_item.index(rule[0]) + 1
                                min_index = rule_item_index if rule_item_index > min_index else min_index
                print(f"wanting to add item {item} in {ordered_item}, index chosen is between {min_index} and {max_index}")
                if min_index != max_index:
                    index = random.randint(min_index, max_index)
                else:
                    index = min_index
                ordered_item = ordered_item[:index] + [item] + ordered_item[index:]

        if check_option(ordered_item, rules):
            ordered_list += [ordered_item]
        else:
            raise AssertionError(f"list {ordered_list} should be ordered but is not")
    return ordered_list

def check_option(possible_option, rules):
    valid = True
    for option_index, option_item in enumerate(possible_option):
        for rule in rules:
            if option_item in rule:
                # rule applies
                if option_item == rule[0]:
                    # rule 1 is not allowed before option index
                    if rule[1] in possible_option[:option_index]:
                        valid = False
                        break
                else:
                    if rule[0] in possible_option[option_index:]:
                        valid = False
                        break
    return valid

def second():
    with open("input_dec_5.txt", "r") as infile:
        lines = infile.readlines()
    order_items, options = parse_indata(lines)
    valid_list = check_options(options, order_items)
    invalid_list = [i for i in options if i not in valid_list]
    invalid = order_invalid(invalid_list, order_items)
    total = 0
    for val in invalid:
        mid_id = len(val)//2
        total += val[mid_id]
    print(f"second total is {total}")

if __name__=="__main__":
    # test_first()
    test_second()
    # main()
    second()
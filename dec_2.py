def main():
    reports = get_reports()
    valid_count = 0
    print(reports)
    for report in reports:
        if is_valid(report):
            valid_count += 1
    print(f"valid count is {valid_count}")

def is_valid(report):
    if report[-1] == report[0]:
        return False
    up = report[-1] > report[0]
    prev = report[0]
    if up:
        for item in report[1:]:
            if item <= prev or item > prev + 3:
                return False
            prev = item
    else:
        for item in report[1:]:
            if item >= prev or item < prev -3:
                return False
            prev = item
    return True

def test():
    assert(is_valid([7,6,4,2,1]))
    assert(False==is_valid([1,2,7,8,9]))
    assert(False==is_valid([9,8,6,2,1]))
    assert(False==is_valid([1,3,2,4,5]))
    assert(False==is_valid([8,6,4,4,1]))
    assert(is_valid([1,3,6,7,9]))


def second():
    reports = get_reports()
    valid_count = 0
    for report in reports:
        valid = False
        for index in range(len(report)):
            part_1 = [] if index == 0 else report[0:index]
            part_2 = report[index+1:]
            sub_rep = part_1 + part_2
            if is_valid(sub_rep):
                valid_count +=1
                break
    print(f"{valid_count} reports are valid with problem dampner")

def get_reports():
    reports = []
    with open("input_dec_2.txt", "r") as infile:
        for line in infile.readlines():
            report = []
            for item in line.split(" "):
                report += [int(item)]
            reports += [report]
    return reports

if __name__=="__main__":
    test()
    main()
    second()
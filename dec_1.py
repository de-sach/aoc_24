def main():
    first, second = get_lists()
    total = 0
    for index in range(len(first)):
        total += abs(first[index] - second[index])
    print(f"total: {total}")

def second():
    first,second = get_lists()
    total = 0
    for i in first:
        total += second.count(i) * i
    print(f"second total: {total}")

def get_lists():
    first = []
    second = []
    with open("input_dec_1.txt", "r") as infile:
        for line in infile.readlines():
            one, two = line.split("   ")
            first += [int(one)]
            second += [int(two)]
    first.sort()
    second.sort()
    return first,second

if __name__=="__main__":
    main()
    second()
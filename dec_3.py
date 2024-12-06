import re

def main():
    contents = get_contents()
    total = calc_part(contents)
    print(f"total is {total}")

def second():
    contents = get_contents()
    parts = contents.split("don't()")
    first = True
    total = 0
    for part in parts:
        if first:
            first = False
            total += calc_part(part)
        else:
            sub_parts = part.split("do()", maxsplit=1)
            if len(sub_parts) > 1:
                total += calc_part(sub_parts[1])
    print(f"total is {total}")

def calc_part(contents):
    parts = re.findall("mul\(\d+,\d+\)", contents)
    total = 0
    for part in parts:
        first, second = part.strip("mul(").strip(")").split(",")
        first, second = int(first), int(second)
        total += first * second
    return total

def get_contents():
    with open("input_dec_3.txt","r") as infile:
        contents = infile.read()
    return contents

if __name__=="__main__":
    main()
    second()
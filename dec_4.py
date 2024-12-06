
def main():
    with open("input_dec_4.txt", "r") as infile:
        contents = infile.read()
    lines = contents.split("\n")
    row_count = len(lines)
    col_count = len(lines[0])
    print(f"x,y: {col_count},{row_count}")
    # direction: horizontal, forward + backward
    count = 0
    for line in lines:
        for i in range(row_count - 3):
            if line[i:i+4] == "XMAS":
                count += 1
            elif line[i:i+4] == "SAMX":
                count += 1
    print(f"horizontal count is {count}")
    for i in range(row_count - 3):
        for j in range(col_count):
            if lines[i][j] == "X" and lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
                count += 1
            if lines[i][j] == "S" and lines[i+1][j] == "A" and lines[i+2][j] == "M" and lines[i+3][j] == "X":
                count += 1
    print(f"horizontal + vertical count is {count}")
    for i in range(row_count):
        # diagonal up
        for j in range(col_count):
            if 0 <= i + 3 < row_count  and 0 <= j - 3 < col_count:
                if lines[i][j] == "X" and lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
                    count += 1
                if lines[i][j] == "S" and lines[i+1][j-1] == "A" and lines[i+2][j-2] == "M" and lines[i+3][j-3] == "X":
                    count += 1
            if 0 <= i + 3 < row_count and 0 <= j+3 < col_count:
                if lines[i][j] == "X" and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
                    count += 1
                if lines[i][j] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M" and lines[i+3][j+3] == "X":
                    count += 1
    print(f"+ diagonal is {count}")

def second():
    with open("input_dec_4.txt", "r") as infile:
        lines = infile.read().split("\n")
    calc(lines)

def calc(lines):
    row_count = len(lines)
    col_count = len(lines[0])
    print(f"x,y: {col_count},{row_count}")
    count = 0
    for row in range(row_count):
        for col in range(col_count):
            # top left -> top right or bottom left
            if row < row_count - 2 and col < col_count - 2:
                if lines[row][col] == 'M' and lines[row+1][col+1] == 'A' and lines[row+2][col+2] == "S":
                    # top right orientation
                    if lines[row][col+2] == 'M' and lines[row+2][col] == "S":
                        # print(f"found top left top right, starting at {row},{col}")
                        count += 1
                    # bottom left orientation
                    if lines[row+2][col] == "M" and lines[row][col+2] == "S":
                        # print(f"found top left bottom left, starting at {row},{col}")
                        count += 1
            # botton right -> top right or bottom left
            if 0 <= row - 2 and 0 <= col - 2:
                if lines[row][col] == "M" and lines[row-1][col-1] =="A" and lines[row-2][col-2] == "S":
                    # top right orientation
                    if lines[row-2][col] == "M" and lines[row][col-2] == "S" :
                        # print(f"bottom right top right, starting at {row},{col}")
                        count += 1
                    # bottom left orientation
                    if lines[row][col-2] == "M" and lines[row-2][col] == "S":
                        # print(f"bottom right bottom left, starting at {row},{col}")
                        count += 1
    print(f"X-MAS count is {count}")

def test_second():
    contents = """\
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........\
"""
    lines = contents.split("\n")
    calc(lines)

if __name__=="__main__":
    main()
    test_second()
    second()

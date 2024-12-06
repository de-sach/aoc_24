SAMPLE_IMPUT='''\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...\
'''
from enum import Enum

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN= 3
    LEFT= 4

def find_guard_pos(contents):
    x,y = 0,0
    for line_index, line in enumerate(contents.split("\n")):
        for col_index, pos in enumerate(line):
            if pos == "^":
                x,y = line_index, col_index
    return x,y

def step(x,y,dir, map):
    inRange = True
    if dir == Direction.UP:
        inRange = x > 0
        xn, yn = x-1, y
        if inRange and map[xn][yn] == '#':
            dir = Direction.RIGHT
            xn, yn = x, y
    elif dir == Direction.RIGHT:
        inRange = (y+1 < len(map[0]))
        xn,yn = x, y + 1
        if inRange and map[xn][yn]=="#":
            dir = Direction.DOWN
            xn,yn = x,y
    elif dir == Direction.DOWN:
        inRange = (x+1<len(map))
        xn,yn = x+1,y
        if inRange and map[xn][yn] == "#":
            dir = Direction.LEFT
            xn,yn = x,y
    elif dir == Direction.LEFT:
        inRange = (y > 0)
        xn,yn = x,y-1
        if inRange and map[xn][yn] == '#':
            dir = Direction.UP
            xn,yn = x,y
    else:
        AssertionError("ïnvalid")
    return xn,yn, dir

def test_1():
    contents = SAMPLE_IMPUT
    x,y = find_guard_pos(contents)
    map = contents.split("\n")
    print(f"found guard at {x},{y}")
    pos_x, pos_y = x, y
    direction = Direction.UP
    positions = []
    while 0 <= pos_x < len(map) and 0 <= pos_y < len(map[0]):
        positions += [(pos_x,pos_y)]
        print(f"at pos {pos_x},{pos_y}")
        pos_x, pos_y, direction = step(pos_x, pos_y, direction, map)
    positions = set(positions)
    print(f"different positions: {len(positions)}")

def loop_obstruction(position, max_steps, x,y,dir,map):
    adapted_map  = map
    # print(f"obstruction at {position}")
    adapted_map[position[0]] = adapted_map[position[0]][:position[1]] + "#" + adapted_map[position[0]][position[1] +1:]
    step_count = 0
    posx,posy = x,y
    start_dir = dir
    loop_path = [(x,y,dir)]
    loop = False
    while step_count < max_steps:
        posx,posy,dir = step(posx,posy,dir,adapted_map)
        cur = (posx,posy,dir)
        if cur in loop_path:
            loop = True
            break
        loop_path += [cur]
        step_count += 1
        if posx < 0 or posx > len(adapted_map):
            break
        if posy < 0 or posy > len(adapted_map[0]):
            break
    return loop


def test_2():
    contents = SAMPLE_IMPUT
    x,y = find_guard_pos(contents)
    map = contents.split("\n")
    print(f"found guard at {x},{y}")
    pos_x, pos_y = x, y
    direction = Direction.UP
    positions = []
    while 0 <= pos_x < len(map) and 0 <= pos_y < len(map[0]):
        positions += [(pos_x,pos_y)]
        # print(f"at pos {pos_x},{pos_y}")
        pos_x, pos_y, direction = step(pos_x, pos_y, direction, map)
    set_positions = set(positions)
    # print(f"different positions: {len(set_positions)}")
    posible_obstruction_count = 0
    print(f"max {len(set_positions)} iterations of {20* len(positions)} steps")
    set_positions.remove((x,y))
    for position in list(set_positions):
        if (loop_obstruction(position, 20*len(positions), x, y, Direction.UP, map[:])):
            posible_obstruction_count += 1
    print(f"posible loop obstructions {posible_obstruction_count}")

def main():
    with open("input_dec_6.txt", "r") as infile:
        contents = infile.read()
    x,y = find_guard_pos(contents)
    map = contents.split("\n")
    print(f"found guard at {x},{y}")
    pos_x, pos_y = x, y
    direction = Direction.UP
    positions = []
    while 0 <= pos_x < len(map) and 0 <= pos_y < len(map[0]):
        positions += [(pos_x,pos_y)]
        print(f"at pos {pos_x},{pos_y}")
        pos_x, pos_y, direction = step(pos_x, pos_y, direction, map)
    positions = set(positions)
    print(f"different positions: {len(positions)}")

def second():
    with open("input_dec_6.txt", "r") as infile:
        contents = infile.read()
    x,y = find_guard_pos(contents)
    map = contents.split("\n")
    print(f"found guard at {x},{y}")
    pos_x, pos_y = x, y
    direction = Direction.UP
    positions = []
    while 0 <= pos_x < len(map) and 0 <= pos_y < len(map[0]):
        positions += [(pos_x,pos_y)]
        # print(f"at pos {pos_x},{pos_y}")
        pos_x, pos_y, direction = step(pos_x, pos_y, direction, map)
    set_positions = set(positions)
    # print(f"different positions: {len(set_positions)}")
    posible_obstruction_count = 0
    print(f"max {len(set_positions)} iterations of {2* len(positions)} steps")
    set_positions.remove((x,y))
    count = 0
    for position in list(set_positions):
        count += 1
        if count % 10 == 0:
            print(f"completed {100*count/len(set_positions)} precent")
        if (loop_obstruction(position, 2*len(positions), x, y, Direction.UP, map[:])):
            posible_obstruction_count += 1
    print(f"posible loop obstructions {posible_obstruction_count}")


if __name__=="__main__":
    # test_1()
    # main()
    test_2()
    second()
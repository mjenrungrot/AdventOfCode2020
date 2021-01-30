import sys
import copy


def extra():
    fp = open("17.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))

    board = {}
    R = len(lines)
    C = len(lines[0])
    for i in range(R):
        for j in range(C):
            if lines[i][j] == '#':
                board[(i, j, 0, 0)] = 1
            else:
                board[(i, j, 0, 0)] = 0

    N_CYCLE = 6
    min_x = 0
    max_x = R - 1
    min_y = 0
    max_y = C - 1
    min_z = 0
    max_z = 0
    min_w = 0
    max_w = 0
    for n_cycle in range(N_CYCLE):
        new_board = {}

        min_x -= 1
        max_x += 1
        min_y -= 1
        max_y += 1
        min_z -= 1
        max_z += 1
        min_w -= 1
        max_w += 1
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                for z in range(min_z - 1, max_z + 2):
                    for w in range(min_w - 1, max_w + 2):
                        is_active = ((x, y, z, w)
                                     in board) and (board[(x, y, z, w)] == 1)
                        count_active = 0
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                for dz in range(-1, 2):
                                    for dw in range(-1, 2):
                                        if abs(dx) + abs(dy) + abs(dz) + abs(
                                                dw) == 0:
                                            continue

                                        if (x + dx, y + dy, z + dz,
                                                w + dw) not in board:
                                            continue

                                        if board[(x + dx, y + dy, z + dz,
                                                  w + dw)] == 1:
                                            count_active += 1

                        if is_active and (count_active == 2 or
                                          count_active == 3):
                            new_board[(x, y, z, w)] = 1
                        elif is_active:
                            new_board[(x, y, z, w)] = 0
                        elif (not is_active) and (count_active == 3):
                            new_board[(x, y, z, w)] = 1
                        else:
                            new_board[(x, y, z, w)] = 0

        board = copy.deepcopy(new_board)

    ans = 0
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                for w in range(min_w - 1, max_w + 2):
                    ans += (x, y, z, w) in board and board[(x, y, z, w)] == 1
    print(ans)


def main():
    fp = open("17.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))

    board = {}
    R = len(lines)
    C = len(lines[0])
    for i in range(R):
        for j in range(C):
            if lines[i][j] == '#':
                board[(i, j, 0)] = 1
            else:
                board[(i, j, 0)] = 0

    N_CYCLE = 6
    min_x = 0
    max_x = R - 1
    min_y = 0
    max_y = C - 1
    min_z = 0
    max_z = 0
    for n_cycle in range(N_CYCLE):
        new_board = {}

        min_x -= 1
        max_x += 1
        min_y -= 1
        max_y += 1
        min_z -= 1
        max_z += 1
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                for z in range(min_z - 1, max_z + 2):
                    is_active = ((x, y, z) in board) and (board[(x, y, z)] == 1)
                    count_active = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):
                                if abs(dx) + abs(dy) + abs(dz) == 0:
                                    continue

                                if (x + dx, y + dy, z + dz) not in board:
                                    continue

                                if board[(x + dx, y + dy, z + dz)] == 1:
                                    count_active += 1

                    if is_active and (count_active == 2 or count_active == 3):
                        new_board[(x, y, z)] = 1
                    elif is_active:
                        new_board[(x, y, z)] = 0
                    elif (not is_active) and (count_active == 3):
                        new_board[(x, y, z)] = 1
                    else:
                        new_board[(x, y, z)] = 0

        board = copy.deepcopy(new_board)

    ans = 0
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                ans += (x, y, z) in board and board[(x, y, z)] == 1
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

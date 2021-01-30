import sys
import copy


def extra():
    fp = open("11.input")
    tables = list(map(lambda x: list(x.strip()), fp.readlines()))
    R = len(tables)
    C = len(tables[0])

    while True:
        new_tables = copy.deepcopy(tables)
        change = False
        for r in range(R):
            for c in range(C):
                if tables[r][c] == '.':
                    continue

                count_occupied = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        found = False
                        if dr == dc == 0:
                            continue
                        for k in range(1, max(R, C)):
                            if 0 <= r + dr * k < R and 0 <= c + dc * k < C:
                                if tables[r + dr * k][c + dc * k] == '#':
                                    found = True
                                    break
                                elif tables[r + dr * k][c + dc * k] == 'L':
                                    break
                            else:
                                break
                        count_occupied += found

                if tables[r][c] == 'L' and count_occupied == 0:
                    new_tables[r][c] = '#'
                    change = True
                elif tables[r][c] == '#' and count_occupied >= 5:
                    new_tables[r][c] = 'L'
                    change = True
                else:
                    new_tables[r][c] = tables[r][c]

        tables = copy.deepcopy(new_tables)

        if not change:
            break

    n_occupied = 0
    for r in range(R):
        for c in range(C):
            n_occupied += (tables[r][c] == '#')
    print(n_occupied)


def main():
    fp = open("11.input")
    tables = list(map(lambda x: list(x.strip()), fp.readlines()))
    R = len(tables)
    C = len(tables[0])

    while True:
        new_tables = copy.deepcopy(tables)
        change = False
        for r in range(R):
            for c in range(C):
                count_occupied = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == dc == 0:
                            continue
                        if 0 <= r + dr < R and 0 <= c + dc < C:
                            count_occupied += (tables[r + dr][c + dc] == '#')
                if tables[r][c] == 'L' and count_occupied == 0:
                    new_tables[r][c] = '#'
                    change = True
                elif tables[r][c] == '#' and count_occupied >= 4:
                    new_tables[r][c] = 'L'
                    change = True
                else:
                    new_tables[r][c] = tables[r][c]

        tables = copy.deepcopy(new_tables)

        if not change:
            break

    n_occupied = 0
    for r in range(R):
        for c in range(C):
            n_occupied += (tables[r][c] == '#')
    print(n_occupied)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

import sys
import copy
import math


def extra():
    fp = open("24.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))

    states = {}
    N_DIGIT = 3
    for line in lines:
        cur = 0
        pos = (0, 0)
        while cur < len(line):
            if line[cur] == 'e':
                x, y = pos
                x += math.cos(0 / 180 * math.pi)
                y += math.sin(0 / 180 * math.pi)
                pos = (x, y)
                cur += 1
            elif line[cur] == 'w':
                x, y = pos
                x += math.cos(180 / 180 * math.pi)
                y += math.sin(180 / 180 * math.pi)
                pos = (x, y)
                cur += 1
            elif line[cur:cur + 2] == "ne":
                x, y = pos
                x += math.cos(60 / 180 * math.pi)
                y += math.sin(60 / 180 * math.pi)
                pos = (x, y)
                cur += 2
            elif line[cur:cur + 2] == "nw":
                x, y = pos
                x += math.cos(120 / 180 * math.pi)
                y += math.sin(120 / 180 * math.pi)
                pos = (x, y)
                cur += 2
            elif line[cur:cur + 2] == "sw":
                x, y = pos
                x += math.cos(240 / 180 * math.pi)
                y += math.sin(240 / 180 * math.pi)
                pos = (x, y)
                cur += 2
            elif line[cur:cur + 2] == "se":
                x, y = pos
                x += math.cos(300 / 180 * math.pi)
                y += math.sin(300 / 180 * math.pi)
                pos = (x, y)
                cur += 2

        x, y = pos
        round_x = round(x, N_DIGIT)
        round_y = round(y, N_DIGIT)
        if (round_x, round_y) not in states:
            states[(round_x, round_y)] = (0, x, y)

        tmp = states[(round_x, round_y)]
        states[(round_x, round_y)] = (1 - tmp[0], x, y)

    def find_neighbors(states):
        neighbors = {}
        for (round_x, round_y) in states:
            neighbors[(round_x, round_y)] = states[(round_x, round_y)]
            _, x, y = states[(round_x, round_y)]

            for angle in [0, 60, 120, 180, 240, 300]:
                new_x = x + math.cos(angle / 180 * math.pi)
                new_y = y + math.sin(angle / 180 * math.pi)

                round_new_x = round(new_x, N_DIGIT)
                round_new_y = round(new_y, N_DIGIT)
                if (round_new_x, round_new_y) in states:
                    continue

                neighbors[(round_new_x, round_new_y)] = (0, new_x, new_y)

        return neighbors

    def update(states, nodes):
        new_states = states.copy()

        for (round_x, round_y) in nodes:
            (color, x, y) = nodes[(round_x, round_y)]

            cnt_black = 0
            for angle in [0, 60, 120, 180, 240, 300]:
                new_x = x + math.cos(angle / 180 * math.pi)
                new_y = y + math.sin(angle / 180 * math.pi)
                round_new_x = round(new_x, N_DIGIT)
                round_new_y = round(new_y, N_DIGIT)
                if (round_new_x, round_new_y) in states:
                    cnt_black += (states[(round_new_x, round_new_y)][0] == 1)

            # black
            if (round_x, round_y) in states and states[(round_x,
                                                        round_y)][0] == 1:
                if cnt_black == 0 or cnt_black > 2:
                    new_states[(round_x, round_y)] = (0, x, y)
                else:
                    new_states[(round_x, round_y)] = (1, x, y)
            # white
            else:
                if (round_x, round_y) not in states:
                    new_states[(round_x, round_y)] = (color, x, y)

                if cnt_black == 2:
                    new_states[(round_x, round_y)] = (1, x, y)
                else:
                    new_states[(round_x, round_y)] = (0, x, y)
        return new_states

    def count_black(states):
        ans = 0
        for (x, y) in states:
            if states[(x, y)][0] == 1:
                ans += 1
        return ans

    N_DAY = 100
    for day in range(1, N_DAY + 1):
        neighbors = find_neighbors(states)
        states = update(states, neighbors)
        # print("Day {}: {}".format(day, count_black(states)))

    ans = count_black(states)
    print(ans)


def main():
    fp = open("24.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))

    states = {}
    for line in lines:
        cur = 0
        pos = (0, 0)
        while cur < len(line):
            if line[cur] == 'e':
                x, y = pos
                x += math.cos(0 / 180 * math.pi)
                y += math.sin(0 / 180 * math.pi)
                pos = (x, y)
                cur += 1
            elif line[cur] == 'w':
                x, y = pos
                x += math.cos(180 / 180 * math.pi)
                y += math.sin(180 / 180 * math.pi)
                pos = (x, y)
                cur += 1
            elif line[cur:cur + 2] == "ne":
                x, y = pos
                x += math.cos(60 / 180 * math.pi)
                y += math.sin(60 / 180 * math.pi)
                pos = (x, y)
                cur += 2
            elif line[cur:cur + 2] == "nw":
                x, y = pos
                x += math.cos(120 / 180 * math.pi)
                y += math.sin(120 / 180 * math.pi)
                pos = (x, y)
                cur += 2
            elif line[cur:cur + 2] == "sw":
                x, y = pos
                x += math.cos(240 / 180 * math.pi)
                y += math.sin(240 / 180 * math.pi)
                pos = (x, y)
                cur += 2
            elif line[cur:cur + 2] == "se":
                x, y = pos
                x += math.cos(300 / 180 * math.pi)
                y += math.sin(300 / 180 * math.pi)
                pos = (x, y)
                cur += 2

        x, y = pos
        x = round(x, 3)
        y = round(y, 3)
        if (x, y) not in states:
            states[(x, y)] = 0

        states[(x, y)] = 1 - states[(x, y)]

    ans = 0
    for (x, y) in states:
        if states[(x, y)] == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

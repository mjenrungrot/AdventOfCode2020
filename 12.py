import sys
import copy
import math


def extra():
    fp = open("12.input")
    commands = list(map(lambda x: (x[0], float(x[1:].strip())), fp.readlines()))

    theta = 0.0  # [0, 2*pi)
    pos = (0, 0)  # (x, y)
    diff = (10, 1)
    for command in commands:
        op = command[0]
        amount = command[1]

        if op == "N":
            new_pos = pos
            diff = (diff[0], diff[1] + amount)
        elif op == "S":
            new_pos = pos
            diff = (diff[0], diff[1] - amount)
        elif op == "E":
            new_pos = pos
            diff = (diff[0] + amount, diff[1])
        elif op == "W":
            new_pos = pos
            diff = (diff[0] - amount, diff[1])
        elif op == "F":
            new_pos = (pos[0] + amount * diff[0], pos[1] + amount * diff[1])
        elif op == "L":
            diff_length = math.sqrt(diff[0]**2 + diff[1]**2)
            diff_angle = math.atan2(diff[1], diff[0])
            new_angle = (diff_angle + amount / 180.0 * math.pi +
                         2 * math.pi) % (2 * math.pi)
            diff = (diff_length * math.cos(new_angle),
                    diff_length * math.sin(new_angle))
            new_pos = pos
        elif op == "R":
            diff_length = math.sqrt(diff[0]**2 + diff[1]**2)
            diff_angle = math.atan2(diff[1], diff[0])
            new_angle = (diff_angle - amount / 180.0 * math.pi +
                         2 * math.pi) % (2 * math.pi)
            diff = (diff_length * math.cos(new_angle),
                    diff_length * math.sin(new_angle))
            new_pos = pos
        diff = (round(diff[0]), round(diff[1]))
        pos = (round(new_pos[0]), round(new_pos[1]))

    ans = int(abs(pos[0]) + abs(pos[1]))
    print(ans)


def main():
    fp = open("12.input")
    commands = list(map(lambda x: (x[0], float(x[1:].strip())), fp.readlines()))

    theta = 0.0  # [0, 2*pi)
    pos = (0, 0)  # (x, y)
    for command in commands:
        op = command[0]
        amount = command[1]

        if op == "N":
            new_pos = (pos[0], pos[1] + amount)
        elif op == "S":
            new_pos = (pos[0], pos[1] - amount)
        elif op == "E":
            new_pos = (pos[0] + amount, pos[1])
        elif op == "W":
            new_pos = (pos[0] - amount, pos[1])
        elif op == "F":
            new_pos = (pos[0] + amount * math.cos(theta),
                       pos[1] + amount * math.sin(theta))
        elif op == "L":
            theta = (theta + amount / 180.0 * math.pi + 2 * math.pi) % (2 *
                                                                        math.pi)
            new_pos = pos
        elif op == "R":
            theta = (theta - amount / 180.0 * math.pi + 2 * math.pi) % (2 *
                                                                        math.pi)
            new_pos = pos

        pos = new_pos

    ans = int(abs(pos[0]) + abs(pos[1]))
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

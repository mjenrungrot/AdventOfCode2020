import sys


def extra():
    fp = open("3.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))
    ans1 = 0
    ans3 = 0
    ans5 = 0
    ans7 = 0
    ans1_2 = 0

    curr1 = 0
    curr3 = 0
    curr5 = 0
    curr7 = 0
    curr1_2 = 0
    for i, line in enumerate(lines):
        if line[curr1] == '#':
            ans1 += 1
        if line[curr3] == '#':
            ans3 += 1
        if line[curr5] == '#':
            ans5 += 1
        if line[curr7] == '#':
            ans7 += 1
        if i % 2 == 0 and line[curr1_2] == '#':
            ans1_2 += 1

        curr1 = (curr1 + 1) % len(line)
        curr3 = (curr3 + 3) % len(line)
        curr5 = (curr5 + 5) % len(line)
        curr7 = (curr7 + 7) % len(line)
        curr1_2 = (curr1_2 + (i % 2 == 0)) % len(line)

    print(ans1 * ans3 * ans5 * ans7 * ans1_2)


def main():
    fp = open("3.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))
    ans = 0

    curr = 0
    for _, line in enumerate(lines):
        if line[curr] == '#':
            ans += 1
        curr = (curr + 3) % len(line)
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

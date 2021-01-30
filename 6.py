import sys


def extra():
    fp = open("6.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))
    ans = 0
    n_prob = 0
    used = {}

    for _, line in enumerate(lines):
        if line == "":
            for key in used:
                if used[key] == n_prob:
                    ans += 1
            n_prob = 0
            used = {}
            continue

        for ch in line:
            if ch not in used:
                used[ch] = 0
            used[ch] += 1
        n_prob += 1

    for key in used:
        if used[key] == n_prob:
            ans += 1
    print(ans)


def main():
    fp = open("6.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))
    ans = 0
    used = set()
    for _, line in enumerate(lines):
        if line == "":
            ans += len(used)
            used = set()
            continue

        for ch in line:
            used.add(ch)

    ans += len(used)
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

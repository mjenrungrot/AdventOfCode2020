import sys


def extra():
    fp = open("4.input")
    lines = list(map(lambda x: x, fp.readlines()))
    lines = ''.join(lines).split('\n\n')
    lines = list(map(lambda x: x.replace('\n', ' ').strip().split(), lines))
    lines = list(map(lambda x: dict(map(lambda y: y.split(':'), x)), lines))

    ans = 0
    valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for _, line in enumerate(lines):
        check = True
        for key in valid_keys:
            if key not in line:
                check = False
                break

        if not check:
            continue

        if not 1920 <= int(line['byr']) <= 2002:
            check = False
        if not 2010 <= int(line['iyr']) <= 2020:
            check = False
        if not 2020 <= int(line['eyr']) <= 2030:
            check = False
        if not (
            (line['hgt'][-2:] == 'cm' and
             150 <= int(line['hgt'][:-2]) <= 193) or
            (line['hgt'][-2:] == 'in' and 59 <= int(line['hgt'][:-2]) <= 76)):
            check = False
        if not len(line['hcl']) == 7:
            check = False
        else:
            if line['hcl'][0] != '#':
                check = False
            for i in range(1, len(line['hcl'])):
                if line['hcl'][i] not in str([str(i) for i in range(10)
                                             ]) + "abcdef":
                    check = False
        if not (line['ecl']
                in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            check = False
        if not len(line['pid']) == 9:
            check = False
        else:
            for i in range(len(line['pid'])):
                if line['pid'][i] not in str([str(i) for i in range(10)]):
                    check = False

        if check:
            ans += 1
    print(ans)


def main():
    fp = open("4.input")
    lines = list(map(lambda x: x, fp.readlines()))
    lines = ''.join(lines).split('\n\n')
    lines = list(map(lambda x: x.replace('\n', ' ').strip().split(), lines))
    lines = list(map(lambda x: dict(map(lambda y: y.split(':'), x)), lines))

    ans = 0
    valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for _, line in enumerate(lines):
        check = True
        for key in valid_keys:
            if key not in line:
                check = False
                break

        if not check:
            continue

        if check:
            ans += 1
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

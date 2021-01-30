import sys


def extra():
    fp = open("2.input")
    inputs = list(map(lambda x: x.strip().split(': '), fp.readlines()))
    ans = 0
    for _, x in enumerate(inputs):
        policy, policy_ch = x[0].split()
        policy1, policy2 = list(map(int, policy.split('-')))

        if (x[1][policy1 - 1] == policy_ch) ^ (x[1][policy2 - 1] == policy_ch):
            ans += 1

    print(ans)


def main():
    fp = open("2.input")
    inputs = list(map(lambda x: x.strip().split(': '), fp.readlines()))
    ans = 0
    for _, x in enumerate(inputs):
        policy, policy_ch = x[0].split()
        policy_min, policy_max = list(map(int, policy.split('-')))
        counter = 0
        for _, input_ch in enumerate(x[1]):
            if input_ch == policy_ch:
                counter += 1
        if policy_min <= counter <= policy_max:
            ans += 1
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

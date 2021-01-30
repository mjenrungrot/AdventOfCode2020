import sys


def extra():
    fp = open("9.input")
    nums = list(map(lambda x: int(x.strip()), fp.readlines()))
    n_preamble = 25
    weakness = None
    for i in range(n_preamble, len(nums)):
        passed = False
        for j in range(i - n_preamble, i):
            for k in range(j + 1, i):
                if nums[j] + nums[k] == nums[i]:
                    passed = True
                    break
            if passed:
                break

        if not passed:
            weakness = nums[i]
            break

    for start in range(len(nums)):
        for end in range(start + 1, len(nums)):
            tmp = 0
            max_val = -1e9
            min_val = 1e9
            for k in range(start, end + 1):
                tmp += nums[k]
                max_val = max(max_val, nums[k])
                min_val = min(min_val, nums[k])
                if tmp > weakness:
                    break
            if tmp > weakness:
                break
            elif tmp == weakness:
                print(f"{max_val+min_val}")
                return


def main():
    fp = open("9.input")
    nums = list(map(lambda x: int(x.strip()), fp.readlines()))
    n_preamble = 25
    for i in range(n_preamble, len(nums)):
        passed = False
        for j in range(i - n_preamble, i):
            for k in range(j + 1, i):
                if nums[j] + nums[k] == nums[i]:
                    passed = True
                    break
            if passed:
                break

        if not passed:
            print(f"{nums[i]}")
            break


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

import sys


def extra():
    fp = open("1.input")
    nums = list(map(lambda x: int(x.strip()), fp.readlines()))
    ans = None
    for i, num_i in enumerate(nums):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if num_i + nums[j] + nums[k] == 2020:
                    ans = nums[i] * nums[j] * nums[k]
                    break
            if ans:
                break
        if ans:
            break
    print(ans)


def main():
    fp = open("1.input")
    nums = list(map(lambda x: int(x.strip()), fp.readlines()))
    ans = None
    for i, num_i in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if num_i + nums[j] == 2020:
                ans = nums[i] * nums[j]
                break
        if ans:
            break
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

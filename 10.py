import sys


def extra():
    fp = open("10.input")
    nums = list(map(lambda x: int(x.strip()), fp.readlines()))
    nums = sorted(nums)

    dp = [0 for _ in range(max(nums) + 1)]
    dp[0] = 1
    for i, num in enumerate(nums):
        if (num - 1 >= 0):
            dp[num] += dp[num - 1]
        if (num - 2 >= 0):
            dp[num] += dp[num - 2]
        if (num - 3 >= 0):
            dp[num] += dp[num - 3]

    print(dp[nums[-1]])


def main():
    fp = open("10.input")
    nums = list(map(lambda x: int(x.strip()), fp.readlines()))
    nums = sorted(nums)

    curr = 0
    count1 = 0
    count3 = 1
    for i, num in enumerate(nums):
        if num - curr == 1:
            count1 += 1
            curr = num
        elif num - curr == 3:
            count3 += 1
            curr = num
        else:
            print("Test")
            pass
    print(count1, count3)
    print(count1 * count3)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

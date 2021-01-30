import sys


def extra():
    fp = open("15.input")
    nums = list(map(int, fp.readline().split(',')))

    FINAL_TURN = 30000000
    memo = {}
    last_spoken_num = None
    for n_turn in range(1, FINAL_TURN + 1):
        if n_turn <= len(nums):
            last_spoken_num = nums[n_turn - 1]
            memo[last_spoken_num] = (n_turn, None)
        else:
            val = memo[last_spoken_num]
            if val[1] is None:
                last_spoken_num = 0
                if last_spoken_num in memo:
                    memo[last_spoken_num] = (n_turn, memo[last_spoken_num][0])
                else:
                    memo[last_spoken_num] = (n_turn, None)
            else:
                last_spoken_num = val[0] - val[1]
                if last_spoken_num in memo:
                    memo[last_spoken_num] = (n_turn, memo[last_spoken_num][0])
                else:
                    memo[last_spoken_num] = (n_turn, None)
    ans = last_spoken_num
    print(ans)


def main():
    fp = open("15.input")
    nums = list(map(int, fp.readline().split(',')))

    FINAL_TURN = 2020
    memo = {}
    last_spoken_num = None
    for n_turn in range(1, FINAL_TURN + 1):
        if n_turn <= len(nums):
            last_spoken_num = nums[n_turn - 1]
            memo[last_spoken_num] = (n_turn, None)
        else:
            val = memo[last_spoken_num]
            if val[1] is None:
                last_spoken_num = 0
                if last_spoken_num in memo:
                    memo[last_spoken_num] = (n_turn, memo[last_spoken_num][0])
                else:
                    memo[last_spoken_num] = (n_turn, None)
            else:
                last_spoken_num = val[0] - val[1]
                if last_spoken_num in memo:
                    memo[last_spoken_num] = (n_turn, memo[last_spoken_num][0])
                else:
                    memo[last_spoken_num] = (n_turn, None)
    ans = last_spoken_num
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

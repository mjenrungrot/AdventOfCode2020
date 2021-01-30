import sys
import copy
import math


def extra():
    fp = open("23.input")
    nums = list(map(int, fp.readline()))
    next_nums = {}
    for i in range(len(nums) - 1):
        next_nums[nums[i]] = nums[i + 1]

    MAX_VAL = 1_000_000
    next_nums[nums[-1]] = 10
    for i in range(10, MAX_VAL):
        next_nums[i] = i + 1
    next_nums[MAX_VAL] = nums[0]

    N_PICKUP = 3
    N_ROUND = 10_000_000
    current = nums[0]
    for n_round in range(N_ROUND):
        if n_round != 0:
            current = next_nums[current]

        one = next_nums[current]
        two = next_nums[one]
        three = next_nums[two]
        pickup = (one, two, three)

        destination = current - 1 if current > 1 else MAX_VAL
        while destination in pickup:
            destination = destination - 1 if destination > 1 else MAX_VAL

        # Fix
        next_nums[current] = next_nums[three]
        next_nums[three] = next_nums[destination]
        next_nums[destination] = one

    ans = next_nums[1] * next_nums[next_nums[1]]
    print(ans)


def main():
    fp = open("23.input")
    nums = list(map(int, fp.readline()))
    curr_cup_idx = 0

    N_PICKUP = 3
    N_ROUND = 100
    for n_round in range(N_ROUND):
        # curr step
        current_val = nums[curr_cup_idx]
        pickups = [
            nums[(curr_cup_idx + x) % len(nums)]
            for x in range(1, N_PICKUP + 1)
        ]
        destination = nums[curr_cup_idx] - 1 if nums[curr_cup_idx] > 1 else 9
        while True:
            if destination in pickups:
                destination = destination - 1 if destination > 1 else 9
            else:
                break
        # print("Round ===> {}".format(n_round + 1))
        # print("Current: [{}] {}".format(nums[curr_cup_idx], nums))
        # print("Pickup: {}".format(pickups))
        # print("Destination: {}".format(destination))

        # move to next step
        for pickup in pickups:
            nums.remove(pickup)

        for i, num in enumerate(nums):
            if num == destination:
                for k, pickup in enumerate(pickups):
                    nums.insert(i + k + 1, pickup)
                break

        for i, num in enumerate(nums):
            if num == current_val:
                curr_cup_idx = i
                break
        curr_cup_idx = (curr_cup_idx + 1) % len(nums)

    pos1 = None
    for i, num in enumerate(nums):
        if num == 1:
            pos1 = i
            break

    ans = []
    for i in range(8):
        ans.append(str(nums[(pos1 + i + 1) % len(nums)]))
    ans = ''.join(ans)
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

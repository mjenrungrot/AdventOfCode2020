import sys
import copy
import math


def extra():
    fp = open("13.input")
    _ = int(fp.readline())
    bus_nums = list(
        map(lambda x: -1 if x == 'x' else int(x),
            fp.readline().strip().split(',')))

    curr_timestamp = 100_000_000_000_000
    curr_timestamp += (bus_nums[0] - curr_timestamp % bus_nums[0])
    curr_bus_idx = 1
    curr_factor = bus_nums[0]
    assert curr_timestamp % bus_nums[0] == 0
    while curr_bus_idx < len(bus_nums):
        if bus_nums[curr_bus_idx] == -1:
            curr_bus_idx += 1
            continue

        if (curr_timestamp + curr_bus_idx) % bus_nums[curr_bus_idx] == 0:
            curr_factor = (curr_factor * bus_nums[curr_bus_idx]) // math.gcd(
                curr_factor, bus_nums[curr_bus_idx])
            curr_bus_idx += 1
            continue

        curr_timestamp += curr_factor

    print(curr_timestamp)


def main():
    fp = open("13.input")
    T = int(fp.readline())
    bus_nums = list(
        map(int, filter(lambda x: x != "x",
                        fp.readline().strip().split(','))))

    curr_timestamp = T
    while True:
        check = False
        for bus_num in bus_nums:
            if curr_timestamp % bus_num == 0:
                check = True
                wait_time = (curr_timestamp - T)
                ans = wait_time * bus_num
                print(ans)
                break
        if check:
            break
        curr_timestamp += 1


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

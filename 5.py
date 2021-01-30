import sys


def extra():
    fp = open("5.input")
    lines = list(map(lambda x: (x.strip()[:7], x.strip()[7:]), fp.readlines()))

    occupied = set()
    max_seat_id = -1
    for _, line in enumerate(lines):
        seat = line[0]
        seat = list(map(lambda ch: int(ch == 'B'), seat))
        base = 64
        row_no = 0
        for _, ch in enumerate(seat):
            row_no += ch * base
            base //= 2

        col = line[1]
        col = list(map(lambda ch: int(ch == 'R'), col))
        base = 4
        col_no = 0
        for _, ch in enumerate(col):
            col_no += ch * base
            base //= 2

        seat_id = row_no * 8 + col_no
        occupied.add(seat_id)
        max_seat_id = max(max_seat_id, seat_id)

    ans = -1
    for i in range(max_seat_id):
        if i not in occupied and (i + 1) in occupied and (i - 1) in occupied:
            ans = i
            break
    print(ans)


def main():
    fp = open("5.input")
    lines = list(map(lambda x: (x.strip()[:7], x.strip()[7:]), fp.readlines()))

    ans = -1
    for _, line in enumerate(lines):
        seat = line[0]
        seat = list(map(lambda ch: int(ch == 'B'), seat))
        base = 64
        row_no = 0
        for _, ch in enumerate(seat):
            row_no += ch * base
            base //= 2

        col = line[1]
        col = list(map(lambda ch: int(ch == 'R'), col))
        base = 4
        col_no = 0
        for _, ch in enumerate(col):
            col_no += ch * base
            base //= 2

        seat_id = row_no * 8 + col_no
        ans = max(ans, seat_id)
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

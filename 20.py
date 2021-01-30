import sys
import copy
import math


def extra():
    fp = open("20.input")
    cards = []

    while True:
        name = fp.readline().strip()
        if name == "":
            break

        card_no = int(name.replace('Tile', '').replace(':', ''))

        contents = [fp.readline().strip() for _ in range(10)]
        fp.readline().strip()

        sides = [
            contents[0],
            ''.join([content[-1] for content in contents]),
            contents[-1][::-1],
            ''.join([content[0] for content in contents[::-1]]),
        ]  # (top, right, bottom, left)

        img_content = [list(x[1:-1]) for x in contents[1:-1]]

        cards.append((card_no, sides, img_content))

    N = int(math.sqrt(len(cards)))

    def rotate(sides, content):
        new_content = copy.deepcopy(content)
        for r in range(len(new_content)):
            for c in range(len(new_content[r])):
                new_content[r][c] = content[c][len(new_content[r]) - r - 1]
        return sides[1:] + [sides[0]], new_content

    def fliph(sides, content):
        new_content = copy.deepcopy(content)
        for r in range(len(new_content)):
            for c in range(len(new_content[r])):
                new_content[r][len(new_content[r]) - c - 1] = content[r][c]
        return [sides[0][::-1], sides[3][::-1], sides[2][::-1],
                sides[1][::-1]], new_content

    global final_assignment
    final_assignment = None

    def dfs(curr_idx, used, assignment):
        global final_assignment
        if final_assignment is not None:
            return

        if curr_idx == N * N:
            final_assignment = assignment.copy()
            return

        R = curr_idx // N
        C = curr_idx % N

        for card in cards:
            card_no, sides, content = card

            if card_no in used:
                continue

            for i in range(8):
                passing = True
                if R > 0 and assignment[(R - 1, C)][0][2] != sides[0][::-1]:
                    passing = False

                if C > 0 and assignment[(R, C - 1)][0][1] != sides[3][::-1]:
                    passing = False

                if passing:
                    used[card_no] = True
                    assignment[(R, C)] = (sides, content, card_no)

                    dfs(curr_idx + 1, used, assignment)
                    del used[card_no]
                    del assignment[(R, C)]
                if final_assignment is not None:
                    return

                sides, content = rotate(sides, content)
                if i == 3:
                    sides, content = fliph(sides, content)

    dfs(0, {}, {})

    PATTERN = ["                  # ", \
               "#    ##    ##    ###", \
               " #  #  #  #  #  #   "]
    bigimg = [[' ' for _ in range(8 * N)] for _ in range(8 * N)]
    for r in range(8 * N):
        for c in range(8 * N):
            img_r = r // 8
            img_c = c // 8
            bigimg[r][c] = final_assignment[(img_r, img_c)][1][r % 8][c % 8]

    for i in range(8):
        _, bigimg = rotate(['', '', '', ''], bigimg)
        if i == 4:
            _, bigimg = fliph(['', '', '', ''], bigimg)

        for r in range(len(bigimg) - len(PATTERN)):
            for c in range(len(bigimg[r]) - len(PATTERN[0])):
                check = True
                for dr in range(len(PATTERN)):
                    for dc in range(len(PATTERN[dr])):
                        if PATTERN[dr][dc] == '#' and bigimg[r + dr][c +
                                                                     dc] == '.':
                            check = False
                            break
                    if not check:
                        break
                if check:
                    for dr in range(len(PATTERN)):
                        for dc in range(len(PATTERN[dr])):
                            if PATTERN[dr][dc] == '#':
                                bigimg[r + dr][c + dc] = 'O'

    ans = 0
    for r in range(len(bigimg)):
        for c in range(len(bigimg[r])):
            ans += bigimg[r][c] == '#'
    print(ans)


def main():
    fp = open("20.input")
    cards = []

    while True:
        name = fp.readline().strip()
        if name == "":
            break

        card_no = int(name.replace('Tile', '').replace(':', ''))

        contents = [fp.readline().strip() for _ in range(10)]
        fp.readline().strip()

        sides = [
            contents[0],
            ''.join([content[-1] for content in contents]),
            contents[-1][::-1],
            ''.join([content[0] for content in contents[::-1]]),
        ]  # (top, right, bottom, left)

        cards.append((card_no, sides))

    N = int(math.sqrt(len(cards)))

    def rotate(sides):
        return sides[1:] + [sides[0]]

    def fliph(sides):
        return [sides[0][::-1], sides[3][::-1], sides[2][::-1], sides[1][::-1]]

    global final_assignment
    final_assignment = None

    def dfs(curr_idx, used, assignment):
        global final_assignment
        if final_assignment is not None:
            return

        if curr_idx == N * N:
            final_assignment = assignment.copy()
            return

        R = curr_idx // N
        C = curr_idx % N

        for card in cards:
            card_no, sides = card

            if card_no in used:
                continue

            for i in range(8):
                passing = True
                if R > 0 and assignment[(R - 1, C)][0][2] != sides[0][::-1]:
                    passing = False

                if C > 0 and assignment[(R, C - 1)][0][1] != sides[3][::-1]:
                    passing = False

                if passing:
                    used[card_no] = True
                    assignment[(R, C)] = (sides, card_no)
                    dfs(curr_idx + 1, used, assignment)
                    del used[card_no]
                    del assignment[(R, C)]
                sides = rotate(sides)
                if i == 3:
                    sides = fliph(sides)

    dfs(0, {}, {})

    ans = final_assignment[(0, 0)][1] * final_assignment[
        (0, N - 1)][1] * final_assignment[(N - 1, 0)][1] * final_assignment[
            (N - 1, N - 1)][1]
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

import sys
from collections import deque
import copy


def extra():
    fp = open("22.input")
    player1 = []
    player2 = []

    fp.readline()  # Read player1
    while True:
        line = fp.readline().strip()
        if line == "":
            break
        player1.append(int(line))

    fp.readline()  # Read player2
    while True:
        line = fp.readline().strip()
        if line == "":
            break
        player2.append(int(line))

    def play(player1, player2):
        player1 = deque(player1)
        player2 = deque(player2)
        memo1 = [player1.copy()]
        memo2 = [player2.copy()]
        n_round = 0

        while len(player1) != 0 and len(player2) != 0:
            if n_round > 0 and player1 in memo1 and player2 in memo2:
                return 1, player1
            memo1.append(player1.copy())
            memo2.append(player2.copy())

            card1 = player1.popleft()
            card2 = player2.popleft()

            if len(player1) >= card1 and len(player2) >= card2:
                t1 = list(player1)[:card1].copy()
                t2 = list(player2)[:card2].copy()
                res, _ = play(t1, t2)
            else:
                res = 1 if card1 > card2 else 2

            if res == 1:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
            n_round += 1

        if len(player1) != 0:
            return 1, player1
        else:
            return 2, player2

    out, winner = play(player1, player2)
    print(winner)

    ans = 0
    for idx, card in enumerate(winner):
        ans += card * (len(winner) - idx)

    print(ans)


def main():
    fp = open("22.input")
    player1 = deque()
    player2 = deque()

    fp.readline()  # Read player1
    while True:
        line = fp.readline().strip()
        if line == "":
            break
        player1.append(int(line))

    fp.readline()  # Read player2
    while True:
        line = fp.readline().strip()
        if line == "":
            break
        player2.append(int(line))

    while len(player1) != 0 and len(player2) != 0:
        card1 = player1.popleft()
        card2 = player2.popleft()

        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        elif card1 < card2:
            player2.append(card2)
            player2.append(card1)

    winner = player1 if len(player1) != 0 else player2
    ans = 0
    for idx, card in enumerate(winner):
        ans += card * (len(winner) - idx)

    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

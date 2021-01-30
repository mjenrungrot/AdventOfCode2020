import sys
import copy
import math


def extra():
    fp = open("25.input")

    SUBJECT_NUMBER = 7
    MODULO = 20201227
    card_public_key = int(fp.readline().strip())
    door_public_key = int(fp.readline().strip())

    # print("card public key = {}".format(card_public_key))
    # print("door public key = {}".format(door_public_key))

    card_loop_size = 0
    curr_num = 1
    while curr_num != card_public_key:
        card_loop_size += 1
        curr_num = (curr_num * SUBJECT_NUMBER) % MODULO
    # print("card loop size: {}".format(card_loop_size))

    door_loop_size = 0
    curr_num = 1
    while curr_num != door_public_key:
        door_loop_size += 1
        curr_num = (curr_num * SUBJECT_NUMBER) % MODULO
    # print("door loop size: {}".format(door_loop_size))

    encryption_key_card_door = 1
    for _ in range(card_loop_size):
        encryption_key_card_door = (encryption_key_card_door *
                                    door_public_key) % MODULO

    encryption_key_door_card = 1
    for _ in range(door_loop_size):
        encryption_key_door_card = (encryption_key_door_card *
                                    card_public_key) % MODULO

    assert encryption_key_card_door == encryption_key_door_card

    ans = encryption_key_card_door
    print(ans)


def main():
    fp = open("25.input")

    SUBJECT_NUMBER = 7
    MODULO = 20201227
    card_public_key = int(fp.readline().strip())
    door_public_key = int(fp.readline().strip())

    # print("card public key = {}".format(card_public_key))
    # print("door public key = {}".format(door_public_key))

    card_loop_size = 0
    curr_num = 1
    while curr_num != card_public_key:
        card_loop_size += 1
        curr_num = (curr_num * SUBJECT_NUMBER) % MODULO
    # print("card loop size: {}".format(card_loop_size))

    door_loop_size = 0
    curr_num = 1
    while curr_num != door_public_key:
        door_loop_size += 1
        curr_num = (curr_num * SUBJECT_NUMBER) % MODULO
    # print("door loop size: {}".format(door_loop_size))

    encryption_key_card_door = 1
    for _ in range(card_loop_size):
        encryption_key_card_door = (encryption_key_card_door *
                                    door_public_key) % MODULO

    encryption_key_door_card = 1
    for _ in range(door_loop_size):
        encryption_key_door_card = (encryption_key_door_card *
                                    card_public_key) % MODULO

    assert encryption_key_card_door == encryption_key_door_card

    ans = encryption_key_card_door
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

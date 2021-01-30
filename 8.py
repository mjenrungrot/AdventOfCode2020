import sys


def parser(line):
    inst, num = line.split()
    num = int(num)
    return inst, num


def extra():

    def runner(insts):
        executed = [False for _ in range(len(insts))]
        curr_pointer = 0
        acc = 0
        while curr_pointer < len(insts):
            if executed[curr_pointer]:
                raise RuntimeError

            inst, num = insts[curr_pointer]
            executed[curr_pointer] = True
            if inst == "nop":
                curr_pointer += 1
            elif inst == "acc":
                acc += num
                curr_pointer += 1
            elif inst == "jmp":
                curr_pointer += num

        return acc

    fp = open("8.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))
    insts = list(map(parser, lines))

    for i, inst in enumerate(insts):
        inst, num = inst
        if inst == "acc":
            continue
        elif inst == "nop":
            insts[i] = ("jmp", num)
            try:
                acc = runner(insts)
                break
            except RuntimeError:
                pass
            insts[i] = ("nop", num)
        elif inst == "jmp":
            insts[i] = ("nop", num)
            try:
                acc = runner(insts)
                break
            except RuntimeError:
                pass
            insts[i] = ("jmp", num)

    print(acc)


def main():
    fp = open("8.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))
    insts = list(map(parser, lines))
    executed = [False for _ in range(len(insts))]
    curr_pointer = 0

    acc = 0
    while curr_pointer < len(insts):
        if executed[curr_pointer]:
            break

        inst, num = insts[curr_pointer]
        executed[curr_pointer] = True
        if inst == "nop":
            curr_pointer += 1
        elif inst == "acc":
            acc += num
            curr_pointer += 1
        elif inst == "jmp":
            curr_pointer += num

    print(acc)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

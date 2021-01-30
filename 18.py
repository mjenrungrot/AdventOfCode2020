import sys
import copy


def extra():
    fp = open("18.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))

    def rank(op):
        if op == '+' or op == '-':
            return 2
        else:
            return 1

    ans = 0
    for line in lines:
        num_stack = []
        op_stack = []

        for ch in line:
            if ch == ' ':
                continue

            if ord('0') <= ord(ch) <= ord('9'):
                num_stack.append(int(ch))
            elif ch == '(':
                op_stack.append(ch)
            elif ch == ')':
                while True:
                    op = op_stack.pop()
                    if op == '(':
                        break

                    r_num = num_stack.pop()
                    l_num = num_stack.pop()

                    output = eval('{} {} {}'.format(l_num, op, r_num))
                    num_stack.append(output)
            else:
                cur_op_rank = rank(ch)

                while len(op_stack) >= 1 and rank(op_stack[-1]) >= cur_op_rank:
                    if op_stack[-1] == '(':
                        break
                    op = op_stack.pop()
                    r_num = num_stack.pop()
                    l_num = num_stack.pop()

                    output = eval('{} {} {}'.format(l_num, op, r_num))
                    num_stack.append(output)

                op_stack.append(ch)

        while len(op_stack) > 0:
            op = op_stack.pop()

            r_num = num_stack.pop()
            l_num = num_stack.pop()

            output = eval('{} {} {}'.format(l_num, op, r_num))
            num_stack.append(output)

        ans += num_stack[0]
    print(ans)


def main():
    fp = open("18.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))

    ans = 0
    for line in lines:
        num_stack = []
        op_stack = []

        for ch in line:
            if ch == ' ':
                continue

            if ord('0') <= ord(ch) <= ord('9'):
                num_stack.append(int(ch))

                while len(num_stack) >= 2 and op_stack[-1] != '(':
                    op = op_stack.pop()
                    r_num = num_stack.pop()
                    l_num = num_stack.pop()

                    output = eval('{} {} {}'.format(l_num, op, r_num))
                    num_stack.append(output)

            elif ch == '(':
                op_stack.append(ch)
            elif ch == ')':
                while True:
                    op = op_stack.pop()
                    if op == '(':
                        break

                    r_num = num_stack.pop()
                    l_num = num_stack.pop()

                    output = eval('{} {} {}'.format(l_num, op, r_num))
                    num_stack.append(output)

                while len(num_stack) >= 2 and op_stack[-1] != '(':
                    op = op_stack.pop()
                    r_num = num_stack.pop()
                    l_num = num_stack.pop()

                    output = eval('{} {} {}'.format(l_num, op, r_num))
                    num_stack.append(output)
            else:
                op_stack.append(ch)

        while len(op_stack) > 0:
            op = op_stack.pop()

            r_num = num_stack.pop()
            l_num = num_stack.pop()

            output = eval('{} {} {}'.format(l_num, op, r_num))
            num_stack.append(output)

        ans += num_stack[0]
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

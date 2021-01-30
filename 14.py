import sys


def extra():

    def apply_mask(value, mask):
        curr = value
        for j, mask_val in enumerate(mask):
            if mask_val == '0':
                continue
            elif mask_val == '1' or mask_val == '+':
                curr |= (1 << j)
            elif mask_val == '-':
                curr &= ~(1 << j)
        return curr

    def recurse(mem, mask, pos, mem_id, value):
        if pos == len(mask):
            mem_id = apply_mask(mem_id, mask)
            mem[mem_id] = value
            return

        if mask[pos] == 'X':
            mask[pos] = '-'
            recurse(mem, mask, pos + 1, mem_id, value)
            mask[pos] = '+'
            recurse(mem, mask, pos + 1, mem_id, value)
            mask[pos] = 'X'
        else:
            recurse(mem, mask, pos + 1, mem_id, value)

    fp = open("14.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))

    mask = None
    mem = {}
    for line in lines:
        tokens = list(map(lambda x: x.strip(), line.split('=')))

        if tokens[0] == 'mask':
            mask = list(tokens[1][::-1])
        else:
            mem_id = int(tokens[0][4:-1])
            value = int(tokens[1])
            recurse(mem, mask, 0, mem_id, value)

    ans = 0
    for mem_id in mem:
        ans += mem[mem_id]
    print(ans)


def main():
    fp = open("14.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))

    mask = None
    mem = {}
    for line in lines:
        tokens = list(map(lambda x: x.strip(), line.split('=')))

        if tokens[0] == 'mask':
            mask = tokens[1][::-1]
        else:
            mem_id = int(tokens[0][4:-1])
            value = int(tokens[1])

            curr = value
            for j, mask_val in enumerate(mask):
                if mask_val == '0':
                    curr &= ~(1 << j)
                if mask_val == '1':
                    curr |= (1 << j)
            mem[mem_id] = curr

    ans = 0
    for mem_id in mem:
        ans += mem[mem_id]
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

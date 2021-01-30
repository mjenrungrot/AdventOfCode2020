import sys


def extra():

    def parser(line):
        tokens = line.split()
        name = ' '.join(tokens[:2])

        tokens = tokens[4:]
        num = 0
        tmp = ""
        output = []

        if ' '.join(tokens) == "no other bags.":
            return name, output

        for token in tokens:
            token = token.replace(',', '')
            token = token.replace('.', '')
            if token == "bags" or token == "bag":
                output.append((num, tmp.strip()))
                tmp = ""
            elif token.isnumeric():
                num = int(token)
            else:
                tmp += token + " "
        return name, output

    rules = {}
    memo = {}

    def dfs(node):
        if node in memo:
            return memo[node]

        if len(rules[node]) == 0:
            memo[node] = 1
            return memo[node]

        ans = 1
        for content in rules[node]:
            ans += content[0] * dfs(content[1])

        memo[node] = ans
        return ans

    fp = open("7.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))
    rules = dict(map(parser, lines))

    print(dfs('shiny gold') - 1)


def main():

    def parser(line):
        tokens = line.split()
        name = ' '.join(tokens[:2])

        tokens = tokens[4:]
        tmp = ""
        output = []
        for token in tokens:
            token = token.replace(',', '')
            token = token.replace('.', '')
            if token == "bags" or token == "bag":
                output.append(tmp.strip())
                tmp = ""
                continue
            elif token.isnumeric():
                continue
            tmp += token + " "
        return name, output

    fp = open("7.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))
    lines = list(map(parser, lines))

    ans = 0
    can_hold = set()
    can_hold.add('shiny gold')
    prev_len_can_hold = 1

    while True:
        for rule in lines:
            name, containing = rule
            if name in can_hold:
                continue
            for content in containing:
                if content in can_hold:
                    can_hold.add(name)
                    break

        if prev_len_can_hold == len(can_hold):
            break
        prev_len_can_hold = len(can_hold)

    print(prev_len_can_hold - 1)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

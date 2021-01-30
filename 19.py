import sys


def extra():
    fp = open("19.input")
    rules = {}

    while True:
        line = fp.readline().strip()
        if line == "":
            break

        rule_id, content = line.split(':')
        content = content.strip()
        if '|' in content:
            content_l, content_r = content.strip().split('|')
            content_l = list(map(int, content_l.strip().split()))
            content_r = list(map(int, content_r.strip().split()))
            rules[int(rule_id)] = [content_l, content_r]
        elif '"' in content:
            content = content.strip().replace('"', '')
            rules[int(rule_id)] = content
        else:
            content = list(map(int, content.strip().split()))
            rules[int(rule_id)] = [content]

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    memo = {}

    def accept(s, rule_id):
        if len(s) == 0:
            return False

        if (s, rule_id) in memo:
            return memo[(s, rule_id)]

        tmp_s = s[:]
        rule = rules[rule_id]
        if isinstance(rule, list):
            if len(rule) == 1:

                if len(rule[0]) == 1:
                    output = accept(s, rule[0][0])
                    memo[(s, rule_id)] = output
                    return output
                elif len(rule[0]) == 2:
                    for split in range(len(s)):
                        t1 = accept(s[:split], rule[0][0])
                        if not t1:
                            continue
                        t2 = accept(s[split:], rule[0][1])
                        if t1 and t2:
                            memo[(s, rule_id)] = True
                            return True
                    memo[(s, rule_id)] = False
                    return False
                elif len(rule[0]) == 3:
                    for split1 in range(len(s)):
                        for split2 in range(split1 + 1, len(s)):
                            t1 = accept(s[:split1], rule[0][0])
                            if not t1:
                                continue
                            t2 = accept(s[split1:split2], rule[0][1])
                            if not t2:
                                continue
                            t3 = accept(s[split2:], rule[0][2])
                            if t1 and t2 and t3:
                                return True
                    return False
                else:
                    raise ValueError("Shouldn't get here")
            else:
                tmp = False
                for tt in range(2):
                    input_s = tmp_s[:]
                    if len(rule[tt]) == 1:
                        output = accept(s, rule[tt][0])
                        tmp |= output
                    elif len(rule[tt]) == 2:
                        for split in range(1, len(s)):
                            t1 = accept(s[:split], rule[tt][0])
                            if not t1:
                                continue
                            t2 = accept(s[split:], rule[tt][1])
                            if t1 and t2:
                                tmp |= True
                    elif len(rule[tt]) == 3:
                        for split1 in range(len(s)):
                            for split2 in range(split1 + 1, len(s)):
                                t1 = accept(s[:split1], rule[tt][0])
                                if not t1:
                                    continue
                                t2 = accept(s[split1:split2], rule[tt][1])
                                if not t2:
                                    continue
                                t3 = accept(s[split2:], rule[tt][2])
                                if t1 and t2 and t3:
                                    tmp |= True
                    else:
                        raise ValueError("Shouldn't get here")
                    if tmp:
                        memo[(s, rule_id)] = tmp
                        return tmp

                memo[(s, rule_id)] = tmp
                return tmp
        else:
            if len(s) != 1:
                return False
            return s[0] == rule[0]

    ans = 0
    while True:
        line = fp.readline().strip()
        if line == "":
            break

        found = accept(line, 0)

        if found:
            print(line)
            ans += 1
    print(ans)


def main():
    fp = open("19.input")
    rules = {}

    while True:
        line = fp.readline().strip()
        if line == "":
            break

        rule_id, content = line.split(':')
        content = content.strip()
        if '|' in content:
            content_l, content_r = content.strip().split('|')
            content_l = list(map(int, content_l.strip().split()))
            content_r = list(map(int, content_r.strip().split()))
            rules[int(rule_id)] = [content_l, content_r]
        elif '"' in content:
            content = content.strip().replace('"', '')
            rules[int(rule_id)] = content
        else:
            content = list(map(int, content.strip().split()))
            rules[int(rule_id)] = [content]

    def parse(s, rule_id):
        tmp_s = s[:]
        rule = rules[rule_id]
        if isinstance(rule, list):
            if len(rule) == 1:
                input_s = tmp_s[:]
                for k in range(len(rule[0])):
                    (errno, output_s) = parse(input_s, rule[0][k])
                    if errno != 0:
                        return (errno, None)
                    input_s = output_s
                return (0, output_s)
            else:
                input_s = tmp_s[:]
                for k in range(len(rule[0])):
                    (errno, output_s) = parse(input_s, rule[0][k])
                    if errno != 0:
                        break
                    input_s = output_s
                if errno == 0:
                    return (0, output_s)

                input_s = tmp_s[:]
                for k in range(len(rule[1])):
                    (errno, output_s) = parse(input_s, rule[1][k])
                    if errno != 0:
                        return (errno, None)
                    input_s = output_s
                return (0, output_s)
        else:
            if len(s) == 0:
                return (1, None)

            if rule == s[0]:
                return (0, s[1:])
            else:
                return (1, None)

    ans = 0
    while True:
        line = fp.readline().strip()
        if line == "":
            break

        (errno, output) = parse(line, 0)

        if errno == 0 and output == "":
            ans += 1
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

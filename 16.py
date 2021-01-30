import sys
import itertools
import copy


def extra():
    fp = open("16.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))
    curr_line_no = 0

    features = {}
    while curr_line_no < len(lines):
        if lines[curr_line_no] == "":
            curr_line_no += 1
            break

        line = lines[curr_line_no]
        feature_name, values = line.split(': ')
        range1, range2 = values.split(' or ')
        range1 = list(map(int, range1.split('-')))
        range2 = list(map(int, range2.split('-')))
        features[feature_name] = (range1, range2)
        curr_line_no += 1

    curr_line_no += 1  # skip "your tickets:"
    my_ticket = list(map(int, lines[curr_line_no].split(',')))
    curr_line_no += 1

    curr_line_no += 1  # skip "nearby tickets:"
    nearby_tickets = []
    curr_line_no += 1  # skip "nearby tickets:"
    while curr_line_no < len(lines):
        nearby_ticket = list(map(int, lines[curr_line_no].split(',')))
        curr_line_no += 1
        nearby_tickets.append(nearby_ticket)

    valid_nearby_tickets = []
    for nearby_ticket in nearby_tickets:
        is_error = False
        for val in nearby_ticket:
            check = False
            for feature in features:
                if features[feature][0][0] <= val <= features[feature][0][1]:
                    check = True
                    break
                if features[feature][1][0] <= val <= features[feature][1][1]:
                    check = True
                    break
            if not check:
                is_error = True
                break
        if not is_error:
            valid_nearby_tickets.append(nearby_ticket)

    # TODO: efficient pruning
    global possible_assignment, possible
    possible_assignment = None
    possible = {}
    feature_keys = list(features.keys())

    def dfs(idx, mask, assignment):
        global possible_assignment, possible
        if possible_assignment is not None:
            return

        if idx >= len(my_ticket):
            possible_assignment = copy.deepcopy(assignment)
            return

        for i in range(len(my_ticket)):
            if mask & (1 << i):
                continue

            # check if ticket[idx] is compatible with features[i]
            if (idx, i) in possible:
                check = possible[(idx, i)]
            else:
                check = True
                feature_key = feature_keys[i]
                feature_ranges = features[feature_key]
                for ticket in valid_nearby_tickets:
                    if feature_ranges[0][0] <= ticket[idx] <= feature_ranges[0][
                            1]:
                        continue
                    if feature_ranges[1][0] <= ticket[idx] <= feature_ranges[1][
                            1]:
                        continue
                    check = False
                    break

                possible[(idx, i)] = check

            if not check:
                continue

            assignment[i] = idx
            dfs(idx + 1, mask | (1 << i), assignment)
            del assignment[i]

    dfs(0, 0, {})

    ans = 1
    for i in range(len(feature_keys)):
        key = feature_keys[i]
        if "departure" in key:
            ans *= my_ticket[possible_assignment[i]]
    print(ans)


def main():
    fp = open("16.input")
    lines = list(map(lambda x: x.strip(), fp.readlines()))
    curr_line_no = 0

    features = {}
    while curr_line_no < len(lines):
        if lines[curr_line_no] == "":
            curr_line_no += 1
            break

        line = lines[curr_line_no]
        feature_name, values = line.split(': ')
        range1, range2 = values.split(' or ')
        range1 = list(map(int, range1.split('-')))
        range2 = list(map(int, range2.split('-')))
        features[feature_name] = (range1, range2)
        curr_line_no += 1

    curr_line_no += 1  # skip "your tickets:"
    my_ticket = list(map(int, lines[curr_line_no].split(',')))
    curr_line_no += 1

    curr_line_no += 1  # skip "nearby tickets:"
    nearby_tickets = []
    curr_line_no += 1  # skip "nearby tickets:"
    while curr_line_no < len(lines):
        nearby_ticket = list(map(int, lines[curr_line_no].split(',')))
        curr_line_no += 1
        nearby_tickets.append(nearby_ticket)

    ans = 0
    for nearby_ticket in nearby_tickets:
        for val in nearby_ticket:
            check = False
            for feature in features:
                if features[feature][0][0] <= val <= features[feature][0][1]:
                    check = True
                    break
                if features[feature][1][0] <= val <= features[feature][1][1]:
                    check = True
                    break
            if not check:
                ans += val
    print(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'extra':
        extra()
    else:
        main()

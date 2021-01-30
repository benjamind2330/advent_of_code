import re


def part_1():
    with open("challenge_2_data") as f:
        result = re.findall("([0-9].*)-([0-9].*) ([a-z]): ([a-z].*)", f.read())

        valid_pass = 0
        for lower, upper, c, pword in result:
            lower = int(lower)
            upper = int(upper)
            num_c = pword.count(c)
            # print("{} -> {} | {} | {} | count: {}".format(lower, upper, c, pword, num_c))
            if num_c >= lower and num_c <= upper:
                valid_pass = valid_pass + 1

    print("P1 Num valid: {}".format(valid_pass))


def part_2():

    with open("challenge_2_data") as f:
        result = re.findall("([0-9].*)-([0-9].*) ([a-z]): ([a-z].*)", f.read())
        valid_pass = 0
        for lower, upper, c, pword in result:
            lower = int(lower) - 1
            upper = int(upper) - 1

            num_chars_in_spot = 0

            if lower >= 0 and lower < len(pword) and pword[lower] == c:
                num_chars_in_spot = num_chars_in_spot + 1

            if upper >= 0 and upper < len(pword) and pword[upper] == c:
                num_chars_in_spot = num_chars_in_spot + 1

            if num_chars_in_spot == 1:
                valid_pass = valid_pass + 1

            # print("{} -> {} | {} | {} | count: {}".format(lower, upper, c, pword, num_c))

    print("P2 Num valid: {}".format(valid_pass))


# part_1()
part_2()

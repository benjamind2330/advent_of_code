from collections import Counter
import numpy as np

def part1():
    with open("challenge_6_data") as f:

        total = np.sum([len(Counter(s.replace("\n", "")).keys()) for s in f.read().split("\n\n")])
        print("Part 1: Total yes answers: {}".format(total))


with open("challenge_6_data") as f:
    answers = [Counter(s) for s in f.read().split("\n\n")]
    
    sum_answers = 0

    for c in answers:
        num_in_group = c["\n"] + 1
        for k in c.keys():
            if k != "\n" and c[k] == num_in_group:
                sum_answers = sum_answers+1
    
    print("Part 2: Total with everyone yes: {}".format(sum_answers))



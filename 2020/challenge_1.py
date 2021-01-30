

with open('challenge_1_data') as f:

    array = [int(line) for line in f]


for i in range(0, len(array) - 2):
    for j in range(i + 1, len(array)-1):
        sum = array[i] + array[j]

        if sum > 2020:
            continue

        for k in range(j+1, len(array)):

            if sum + array[k] == 2020:

                print("Found {} at {} and {} at {} and {} at {}, together they are {}".format(
                    array[i], i, array[j], j, array[k], k, array[i]*array[j]*array[k]))
                exit()


print("NOTHING")

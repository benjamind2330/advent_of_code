

with open("challenge_3_data") as f:
    map = f.read().split("\n")
    # print(len(map))
    increments = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    col_length = len(map[0])
    trees_multiplied = 1

    for row_increment, col_increment in increments:
        row = 0
        col = 0
        trees = 0

        while row < len(map):
            if map[row][col % col_length] == '#':
                trees = trees + 1

            row = row + row_increment
            col = col + col_increment

        trees_multiplied = trees_multiplied * trees

        print("Number of trees: {}".format(trees))

    print("Multipled: {}".format(trees_multiplied))

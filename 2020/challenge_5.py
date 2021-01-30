
def binaryDivide(s, upperChar, range):
    for i in s:
        if i == upperChar:
            range[1] = range[0] + (range[1] - range[0]) / 2
        else:
            range[0] = range[0] + (range[1] - range[0]) / 2 + 1
    return range[0]

with open("challenge_5_data") as f:
    seats = []
    maxId = 0
    for line in f:
        
        line = line.strip()
        row = binaryDivide(line[:-3], 'F', [0, 127])
        col = binaryDivide(line[-3:], 'L', [0, 7])
        id = 8*row + col
        maxId = max(maxId, id)
        seats.append(id)

    seats.sort()
    for i in range(0, len(seats) - 1):
        if seats[i+1] - seats[i] > 1:
            mySeat = seats[i] + 1
            break
            

print("Part 1: ", maxId)
print("Part 2: ", mySeat)
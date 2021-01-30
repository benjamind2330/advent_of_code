

class Node:

    def __init__(self):
        contains = []
        top_level = false

with open("challenge_7_data") as f:
    for line in f:
        (top, contains) = line.split("bags contain")
        
        contains.split("bags,", "bag,")
        # print(top, contains)
        Node n
from collections import Counter

with open("input.txt", "r") as f:
    lines = f.readlines()

def partOne(lines):
    distance = 0
    left = []
    right = []

    for line in lines:
        left.append(int(line[0:5]))
        right.append(int(line[8:]))

    sortedLeft = sorted(left)
    sortedRight = sorted(right)

    for i in range(len(sortedLeft)):
        distance += abs(sortedLeft[i] - sortedRight[i])

    print(distance)

def partTwo(lines):
    similarity = 0
    left = []
    right = []

    for line in lines:
        left.append(int(line[0:5]))
        right.append(int(line[8:]))

    rightCounts = Counter(right)

    for i in left:
        similarity += i * rightCounts[i]

    print(similarity)

partOne(f)
partTwo(f)

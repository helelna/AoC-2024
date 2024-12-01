from collections import Counter

f = open("input.txt", "r").readlines()

def partOne(f):
    distance = 0
    left = []
    right = []

    for line in f:
        left.append(int(line[0:5]))
        right.append(int(line[8:]))

    sortedLeft = sorted(left)
    sortedRight = sorted(right)

    for i in range(len(sortedLeft)):
        distance += abs(sortedLeft[i] - sortedRight[i])

    print(distance)

def partTwo(f):
    similarity = 0
    left = []
    right = []

    for line in f:
        left.append(int(line[0:5]))
        right.append(int(line[8:]))

    rightCounts = Counter(right)

    for i in left:
        similarity += i * rightCounts[i]

    print(similarity)

partOne(f)
partTwo(f)

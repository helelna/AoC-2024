import itertools as it

with open("input.txt", "r") as f:
    lines = f.readlines()

def partOne(lines):
    safeCount = 0

    for line in lines:
        levels = [int(i) for i in line.split()]

        if levels == sorted(levels) or levels == sorted(levels, reverse=True):
            for n1, n2 in it.pairwise(levels):
                difference = abs(n1 - n2)
                if difference == 0 or difference > 3:
                    break
            else:
                safeCount += 1

    print(safeCount)

def partTwo(lines):
    safeCount = 0

    for line in lines:
        levels = [int(i) for i in line.split()]
        
        for index in range(len(levels)):
            newLevels = levels[:index] + levels[index+1:]

            if newLevels == sorted(newLevels) or newLevels == sorted(newLevels, reverse=True):
                for n1, n2 in it.pairwise(newLevels):
                    difference = abs(n1 - n2)
                    if difference == 0 or difference > 3:
                        break
                else:
                    safeCount += 1
                    break

    print(safeCount)

partOne(lines)
partTwo(lines)

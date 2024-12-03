import itertools as it
import re

with open("input.txt", "r") as f:
    lines = f.read()

def partOne(lines):
    result = 0

    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    numbers = pattern.findall(lines)

    for x, y in numbers:
        result += int(x) * int(y)

    print(result)

def partTwo(lines):
    result = 0

    doDontPattern = re.compile(r"(?<=don't\(\))[\s\S]*?(?=do\(\))")
    lines = re.sub(doDontPattern, "", lines)

    mulPattern = re.compile(r"mul\((\d+),(\d+)\)")
    numbers = mulPattern.findall(lines)

    for x, y in numbers:
        result += int(x) * int(y)

    print(result)

partOne(lines)
partTwo(lines)

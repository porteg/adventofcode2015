import re
import json

def number12_1():
    dataFile = open("data/day12.txt", "r")

    total = 0

    for line in dataFile:
        s_line = line.replace("\n", "")

        res = re.findall("(-?[0-9]+)", s_line)

        if len(res) > 0:
            res = list(map(int, res))
            total += sum(res)

    print("Result day 12 part 1: " + str(total))

def cleanObject(element):
    x = type(element)
    print(x)


def number12_2():
    dataFile = open("data/day12.txt", "r")

    total = 0

    for line in dataFile:
        s_line = line.replace("\n", "")
        res =json.loads(s_line)

        for element in res:
            new = cleanObject(element)

            x = 1

number12_1()
number12_2()
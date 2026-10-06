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

def cleanObject(element, recursive):
    if isinstance(element, list):
        for i in range(0, len(element)):
            aux_1 = element[i]        
            if not isinstance(aux_1, str) and not isinstance(aux_1, int):
                if isinstance(aux_1, list):
                    res = cleanObject(aux_1, False)
                else: # is a dict()
                    res = cleanObject(aux_1, True)
                    if res[0]:
                        element[i] = dict()                                    
    else: # is a dict()
        found = False

        for key in element.keys():
            if isinstance(element[key], str): # it could be red
                if element[key] == "red": # found, so the caller must empty the label owner
                    return (True, '')
            elif not isinstance(element[key], int):
                aux_1 = element[key]
                if isinstance(aux_1, list):
                    res = cleanObject(aux_1, False)
                else: # is a dict()
                    res = cleanObject(aux_1, True)
                    if res[0]:
                        element[key] = dict()

        if found and recursive:
            return (True, '')

    return (False, '')             


def number12_2():
    dataFile = open("data/day12.txt", "r")

    total = 0

    for line in dataFile:
        s_line = line.replace("\n", "")
        res =json.loads(s_line)

        for element in res:            
            cleanObject(element, False)

    s_line = json.dumps(res)
    res = re.findall("(-?[0-9]+)", s_line)
    
    if len(res) > 0:
        res = list(map(int, res))
        total += sum(res)
    
    print("Result day 12 part 2: " + str(total))

number12_1()
number12_2()
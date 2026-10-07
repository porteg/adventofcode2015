from itertools import permutations

GAIN = "gain"
LOSE = "lose"
MY_SELF = "my_self"

def number13_1():
    people = dict()

    dataFile = open("data/day13.txt", "r")

    for s_line in dataFile:
        s_line = s_line.replace("\n", "")
        s_line = s_line.replace(".", "")
        v_line = s_line.split(" ")

        person_1 = v_line[0]
        person_2 = v_line[-1]

        i_value = int(v_line[3])
        if LOSE in v_line:
            i_value = i_value * -1

        if not person_1 in people.keys(): 
            people[person_1] = dict()

        people[person_1][person_2] = i_value

    options = permutations(people.keys())

    happiness = -1
    best_option = None
    for option in options:
        total_option = 0
        for i in range(0, len(option)):
            member_1 = option[i]
            if i == len(option) - 1:
                member_2 = option[0]
            else:
                member_2 = option[i + 1]

            total_option += people[member_1][member_2]
            total_option += people[member_2][member_1]
        if total_option > happiness:
            best_option = option
            happiness = total_option

    print("Result Day 13 part 1: Happiness total " + str(happiness))

def number13_2():
    people = dict()

    dataFile = open("data/day13.txt", "r")

    for s_line in dataFile:
        s_line = s_line.replace("\n", "")
        s_line = s_line.replace(".", "")
        v_line = s_line.split(" ")

        person_1 = v_line[0]
        person_2 = v_line[-1]

        i_value = int(v_line[3])
        if LOSE in v_line:
            i_value = i_value * -1

        if not person_1 in people.keys(): 
            people[person_1] = dict()

        people[person_1][person_2] = i_value

    people[MY_SELF] = dict()
    for key in people.keys():
        if key != MY_SELF:
            people[key][MY_SELF] = 0
            people[MY_SELF][key] = 0

    options = permutations(people.keys())

    happiness = None
    best_option = None
    for option in options:
        total_option = 0
        for i in range(0, len(option)):
            member_1 = option[i]
            if i == len(option) - 1:
                member_2 = option[0]
            else:
                member_2 = option[i + 1]

            total_option += people[member_1][member_2]
            total_option += people[member_2][member_1]
        if happiness == None or total_option > happiness:
            best_option = option
            happiness = total_option

    print("Result Day 13 part 2: Happiness total " + str(happiness))

number13_1()
number13_2()
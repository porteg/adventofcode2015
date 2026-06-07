UP = "("
DOWN = ")"
BASEMENT = -1

def number1_1():
    dataFile = open("data/day1.txt", "r")
   
    s_line = dataFile.readline().replace("\n", "")

    i_up = s_line.count("(")
    i_down = s_line.count(")")

    i_floor = i_up - i_down

    print("Result day 1 part 1: The floor is " + str(i_floor))


def number1_2():
    dataFile = open("data/day1.txt", "r")

    s_line = dataFile.readline().replace("\n", "")

    l_line = list(s_line)
    i_floor = 0
    i_index = 0
    for direction in l_line:
        i_index += 1
        if direction == UP:
            i_floor += 1
        else:
            i_floor -= 1
        
        if i_floor == BASEMENT:
            break

    print("Result day 1 part 2: The first time in basement is a character number " + str(i_index))

number1_1()
number1_2()
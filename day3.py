UP = "^"
DOWN = "v"
LEFT = "<"
RIGH = ">"

def number3_1():
    dataFile = open("data/day3.txt", "r")
    
    s_line = dataFile.readline().replace("\n", "")

    x, y = (0, 0)
    houses = [(x, y)]

    l_line = list(s_line)
    for move in l_line:
        if move == UP:
            y += 1
        if move == DOWN:
            y -=1
        if move == LEFT:
            x -= 1
        if move == RIGH:
            x += 1

        if not (x, y) in houses:
            houses.append((x, y))

    print("Result day 3 part 1: The number of houses with at least one present are " + str(len(houses)))

def number3_2():
    dataFile = open("data/day3.txt", "r")
    
    s_line = dataFile.readline().replace("\n", "")

    santa_x, santa_y = (0, 0)
    robot_x, robot_y = (0, 0)
    houses = [(santa_x, santa_y)]

    santa_turn = True
    l_line = list(s_line)
    for move in l_line:
        if move == UP:
            if santa_turn:
                santa_y += 1
            else:
                robot_y += 1
        if move == DOWN:
            if santa_turn:
                santa_y -=1
            else:
                robot_y -= 1
        if move == LEFT:
            if santa_turn:
                santa_x -= 1
            else:
                robot_x -= 1
        if move == RIGH:
            if santa_turn:
                santa_x += 1
            else:
                robot_x += 1
        
        if santa_turn:
            if not (santa_x, santa_y) in houses:
                houses.append((santa_x, santa_y))
        else:
            if not (robot_x, robot_y) in houses:
                houses.append((robot_x, robot_y))
            
        santa_turn = not santa_turn
    
    print("Result day 3 part 2: The number of houses with at least one present are " + str(len(houses)))

number3_1()
number3_2()
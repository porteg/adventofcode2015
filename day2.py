def number2_1():
    dataFile = open("data/day2.txt", "r")

    total_paper = 0
    for line in dataFile:
        s_line = line.replace("\n", "")
        l, w, h = s_line.split("x")
        i_l = int(l)
        i_w = int(w)
        i_h = int(h)

        l_sides = [i_l * i_w, i_l * i_h, i_w * i_h]
        i_min = min(l_sides)
        i_paper = sum(l_sides) * 2 + i_min

        total_paper += i_paper

    print("Result day 2 part 1: The ammount of paper required is " + str(total_paper))

def number2_2():
    dataFile = open("data/day2.txt", "r")

    total_ribbon = 0
    for line in dataFile:
        s_line = line.replace("\n", "")
        l, w, h = s_line.split("x")
        i_l = int(l)
        i_w = int(w)
        i_h = int(h)

        ribbon_options =  [2 * (i_l + i_w), 2* (i_l + i_h), 2* (i_w + i_h)]
        ribbon_length = min(ribbon_options) + i_l * i_w * i_h

        total_ribbon += ribbon_length
    
    print("Result day 2 part 2: The ammount of ribbon required is " + str(total_ribbon))


number2_1()
number2_2()
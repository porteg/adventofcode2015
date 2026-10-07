SPEED = "speed"
RUNNING = "running_time"
REST = "rest_time"
SCORE = "score"

TOTAL_TIME_PART_1 = 2503

def number14_2():
    dataFile = open("data/day14.txt", "r")

    reindeers = dict()
    for s_line in dataFile:
        s_line = s_line.replace(".\n", "")

        v_line = s_line.split(" ")
        name = v_line[0]
        speed = int(v_line[3])
        running_time = int(v_line[6])
        rest_time = int(v_line[-2])

        reindeers[name] = dict()
        reindeers[name][SPEED] = speed
        reindeers[name][RUNNING] = running_time
        reindeers[name][REST] = rest_time
        reindeers[name][SCORE] = 0

    r_names = list(reindeers.keys())
    for second in range(1, TOTAL_TIME_PART_1 + 1):
        leader = ""
        km_leader = 0
        km_run = []
        for name in r_names:
            reindeer = reindeers[name]
            gap = reindeer[RUNNING] + reindeer[REST]
            cycles = second // gap
            time_to_complete = second % gap
            running_time = cycles * reindeer[RUNNING]
            if time_to_complete <= reindeer[RUNNING]:
                running_time += time_to_complete
            else:
                running_time += reindeer[RUNNING]

            km_run.append(running_time * reindeer[SPEED])

        l_scores = []
        best_value = max(km_run)
        for i in range(0, len(km_run)):
            if km_run[i] == best_value:
                reindeers[r_names[i]][SCORE] += 1
            l_scores.append(reindeers[r_names[i]][SCORE])


    print("Result Day 14 part 2: The score of the winner " + leader + " has been " + str(max(l_scores)))


def number14_1():
    dataFile = open("data/day14.txt", "r")

    reindeers = dict()
    for s_line in dataFile:
        s_line = s_line.replace(".\n", "")

        v_line = s_line.split(" ")
        name = v_line[0]
        speed = int(v_line[3])
        running_time = int(v_line[6])
        rest_time = int(v_line[-2])

        reindeers[name] = dict()
        reindeers[name][SPEED] = speed
        reindeers[name][RUNNING] = running_time
        reindeers[name][REST] = rest_time

    winner_name = ""
    winner_km = 0

    for name in reindeers.keys():
        reindeer = reindeers[name]
        gap = reindeer[RUNNING] + reindeer[REST]

        cycles = TOTAL_TIME_PART_1 // gap
        time_to_complete = TOTAL_TIME_PART_1 - (cycles * gap)
        running_time = cycles * reindeer[RUNNING]
        if time_to_complete <= reindeer[RUNNING]:
            running_time += time_to_complete
        else:
            running_time += reindeer[RUNNING]

        km_run = running_time * reindeer[SPEED]
        if km_run > winner_km:
            winner_km = km_run
            winner_name = name

    print("Result Day 14 part 1: The distance traveled by the winner " + winner_name + " has been " + str(winner_km))

number14_1()
number14_2()


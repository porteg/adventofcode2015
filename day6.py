TURN_ON = "turn on"
TOGGLE = "toggle"
TURN_OFF = "turn off"
MAX = 1000
ON = 1
OFF = 0

def number6():
    dataFile = open("data/day6.txt", "r")
    
    lights = []
    lights_2 = []
    for i in range(0, MAX):
        lights.append([])
        lights_2.append([])
        for j in range(0, MAX):
            lights[i].append(OFF)
            lights_2[i].append(OFF)
    
    for line in dataFile:
        s_line = line.replace("\n", "")
        
        if s_line.startswith(TOGGLE):
            operation, start_p, sep, end_p = s_line.split(" ")
        else:
            operation_1, operation_2, start_p, sep, end_p = s_line.split(" ")
            operation = operation_1 + " " + operation_2
        
        start_x, start_y = list(map(int, start_p.split(",")))
        end_x, end_y = list(map(int, end_p.split(",")))
        
        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                if operation == TURN_ON:
                    lights[i][j] = ON
                    lights_2[i][j] += 1
                elif operation == TURN_OFF:
                    lights[i][j] = OFF
                    if lights_2[i][j] > 0:
                        lights_2[i][j] -= 1
                else:
                    if lights[i][j] == OFF:
                        lights[i][j] = ON
                    else:
                        lights[i][j] = OFF
                    lights_2[i][j] += 2
        
    total = 0
    total_2 = 0
    for i in range(0, MAX):
        for j in range(0, MAX):
            if lights[i][j] == ON:
                total += 1
            total_2 += lights_2[i][j]
                
    print("Result day 5 part 1: The number of lights on is " + str(total))
    print("Result day 5 part 2: The number of lights on is " + str(total_2))
    
number6()
ON = "#"
OFF = "."

def getLights(grid, state):
    i_lights = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == state:
                i_lights += 1
    
    return i_lights

def turnOn(grid, row, col):
    i_on = 0
    for i in [row - 1, row, row + 1]:
        for j in [col - 1, col, col + 1]:
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
                if not (i == row and j == col):
                    if grid[i][j] == ON:
                        i_on += 1
            
    if grid[row][col] == ON:
        return i_on in [2, 3]
    else:
        return i_on == 3

def number18_1():
    dataFile = open("data/day18.txt", "r")
    
    current_grid = []
    
    for s_line in dataFile:
        s_line = s_line.replace("\n", "")
        current_grid.append(list(s_line))

    steps = 100
    
    for time in range(0, steps):
        aux_grid = []
        for row in range(0, len(current_grid)):
            aux_grid.append(current_grid[row].copy())
            
        for row in range(0, len(current_grid)):
            for col in range(0, len(current_grid[0])):
                if turnOn(current_grid, row, col):
                    aux_grid[row][col] = ON
                else:
                    aux_grid[row][col] = OFF
        
        current_grid = []
        for row in range(0, len(aux_grid)):
            current_grid.append(aux_grid[row].copy())
            
    i_ligths_on = getLights(current_grid, ON)
    
    print("Day 18 part 1: Number of lights ON -> " + str(i_ligths_on))
    
number18_1()

EGGNOG = 150

def generateCombinations(containers, eggnog, currentComb, totalComb):
    comb_aux = totalComb.copy()
    if eggnog > containers[0]:
        auxCurrent = currentComb.copy()
        auxCurrent.append(containers[0])
        if len(containers) > 1:
            comb_aux = generateCombinations(containers[1:], eggnog - containers[0], auxCurrent.copy(), totalComb.copy())
    elif eggnog == containers[0]:
        aux_current = currentComb.copy()
        aux_current.append(containers[0])
        comb_aux = totalComb.copy()
        comb_aux.append(aux_current)
            
    if len(containers) > 1:
        if comb_aux != None:
            comb_aux = generateCombinations(containers[1:], eggnog, currentComb.copy(), comb_aux.copy())
        else:
            comb_aux = generateCombinations(containers[1:], eggnog, currentComb.copy(), totalComb.copy())
                    
    return comb_aux.copy()

def generateMinimumCombinations(containers, eggnog, currentComb, totalComb):
    comb_aux = totalComb.copy()
    if eggnog > containers[0]:
        auxCurrent = currentComb.copy()
        auxCurrent.append(containers[0])
        if len(totalComb) == 0 or len(totalComb[0]) > len(auxCurrent):
            if len(containers) > 1:
                comb_aux = generateMinimumCombinations(containers[1:], eggnog - containers[0], auxCurrent.copy(), totalComb.copy())
    elif eggnog == containers[0]:
        aux_current = currentComb.copy()
        aux_current.append(containers[0])
        if len(totalComb) == 0 or len(totalComb[0]) == len(aux_current):
            comb_aux = totalComb.copy()
            comb_aux.append(aux_current)
        elif len(totalComb[0]) > len(aux_current):
            comb_aux = [aux_current]

    if len(containers) > 1:
        if comb_aux != None:
            comb_aux = generateMinimumCombinations(containers[1:], eggnog, currentComb.copy(), comb_aux.copy())
        else:
            comb_aux = generateMinimumCombinations(containers[1:], eggnog, currentComb.copy(), totalComb.copy())
                    
    return comb_aux.copy()
        

def number17_1():
    dataFile = open("data/day17.txt", "r")
    
    containers = []
    for s_line in dataFile:
        s_line = s_line.replace("\n", "")
        containers.append(int(s_line))
        
    containers.sort(reverse=True)
    eggnog = EGGNOG
    
    combinations = generateCombinations(containers, eggnog, [], [])
        
    print("Day 17 part 1: Number of combinations -> " + str(len(combinations)))
    
def number17_2():
    dataFile = open("data/day17.txt", "r")
    
    containers = []
    for s_line in dataFile:
        s_line = s_line.replace("\n", "")
        containers.append(int(s_line))
        
    containers.sort(reverse=True)
    eggnog = EGGNOG
    
    combinations = generateMinimumCombinations(containers, eggnog, [], [])
        
    print("Day 17 part 2: Number of combinations -> " + str(len(combinations)))
    
number17_1()
number17_2()
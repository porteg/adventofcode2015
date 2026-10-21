def calibrate(molecule, rules):
    molecules = set()
    
    for key, value in rules: 
        prefix = ""
        suffix = molecule
        aux = list(suffix)
        while key in suffix: 
            res = suffix.find(key)
            prefix_aux = prefix + "".join(aux[:res])
            prefix = prefix + "".join(aux[:res + len(key)])
            suffix = "".join(aux[res + len(key):])
            aux_m = prefix_aux + value + suffix
            molecules.add(aux_m)
            
            aux = list(suffix)
            
            
    return len(molecules)

def number19_1():
    dataFile = open("data/day19.txt", "r")
    
    rules = []
    readingRules = True
    molecule = ""
    for s_line in dataFile:
        s_line = s_line.replace("\n", "")
        if s_line == "":
            readingRules = False
        else:
            if readingRules:
                v_line = s_line.split(" => ")
                rules.append((v_line[0], v_line[1]))
            else:
                molecule = s_line
    
    res = calibrate(molecule, rules)
    print("Day 19 part 1: Number of molecules " + str(res)) 
        
number19_1()
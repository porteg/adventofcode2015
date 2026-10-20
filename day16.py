SEPARATOR_TWO_POINTS = ": "
SEPARATOR_COMMA = ", "

def number16_1():
    dataFile = open("data/day16.txt", "r")
    
    aunts = []
    for s_line in dataFile:
        s_line = s_line.replace("\n", "")
        
        pos = s_line.find(SEPARATOR_TWO_POINTS)
        s_line = s_line[pos + len(SEPARATOR_TWO_POINTS):]
        
        v_aunt = s_line.split(SEPARATOR_COMMA)
        d_aunt = {}
        for entry in v_aunt:
            v_entry = entry.split(SEPARATOR_TWO_POINTS)
            d_aunt[v_entry[0]] = int(v_entry[1])
        
        aunts.append(d_aunt)
        
    # data to search 
    my_aunt = {}
    my_aunt["children"] = 3
    my_aunt["cats"] = 7
    my_aunt["samoyeds"] = 2
    my_aunt["pomeranians"] = 3
    my_aunt["akitas"] = 0
    my_aunt["vizslas"] = 0
    my_aunt["goldfish"] = 5
    my_aunt["trees"] = 3
    my_aunt["cars"] = 2
    my_aunt["perfumes"] = 1
    
    for i in range(0, len(aunts)):
        is_aunt = True
        for key in my_aunt.keys():
            if key in aunts[i].keys():
                if aunts[i][key] != my_aunt[key]: # too much elements
                    is_aunt = False
                    break
        if is_aunt: 
            print("Result Day 16 Part 1: Aunt Sue number " + str(i + 1))
            break
        
def number16_2():
    dataFile = open("data/day16.txt", "r")
    
    aunts = []
    for s_line in dataFile:
        s_line = s_line.replace("\n", "")
        
        pos = s_line.find(SEPARATOR_TWO_POINTS)
        s_line = s_line[pos + len(SEPARATOR_TWO_POINTS):]
        
        v_aunt = s_line.split(SEPARATOR_COMMA)
        d_aunt = {}
        for entry in v_aunt:
            v_entry = entry.split(SEPARATOR_TWO_POINTS)
            d_aunt[v_entry[0]] = int(v_entry[1])
        
        aunts.append(d_aunt)
        
    # data to search 
    my_aunt = {}
    my_aunt["children"] = 3
    my_aunt["cats"] = 7
    my_aunt["samoyeds"] = 2
    my_aunt["pomeranians"] = 3
    my_aunt["akitas"] = 0
    my_aunt["vizslas"] = 0
    my_aunt["goldfish"] = 5
    my_aunt["trees"] = 3
    my_aunt["cars"] = 2
    my_aunt["perfumes"] = 1
    
    for i in range(0, len(aunts)):
        is_aunt = True
        for key in my_aunt.keys():
            if key in aunts[i].keys():
                if key in ["cats", "trees"]:
                    if aunts[i][key] <= my_aunt[key]: # not enough
                        is_aunt = False
                        break
                elif key in ["pomeranians", "goldfish"]:
                    if aunts[i][key] > my_aunt[key]: # too much
                        is_aunt = False
                        break                
                else:
                    if aunts[i][key] != my_aunt[key]: 
                        is_aunt = False
                        break
        if is_aunt: 
            print("Result Day 16 Part 2: Aunt Sue number " + str(i + 1))
            break        
        
number16_1()
number16_2()

            
        
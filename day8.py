def encode(chain):
    s_chain = chain[1:-1]
    s_chain = s_chain.replace("\\", "\\\\")
    s_chain = s_chain.replace("\"", "\\\"")
    s_chain = chain[0] + "\\\"" + s_chain + "\\\"" + chain[-1]
    
    return s_chain

def getNumberOfCharacters(chain):
    current = ""
    total = 0
    i = 0
    s_chain = chain[1:-1]
    while i < len(s_chain):
        aux = s_chain[i]
        if current == "":
            if aux.isalpha(): 
                total += 1
            else: 
                current = aux
        elif current == "\\":
            if aux == "x":
                current = current + aux
            else:
                current = ""
                total += 1
        elif current == "\\x":
            current = ""
            value = aux + s_chain[i + 1]
            char = chr(int(value, 16))
            i += 1
            total += 1            
            
        i += 1
    
    return total           

def number8_1():
    dataFile = open("data/day8.txt", "r")
    
    total = 0
    total_chars = 0
    for line in dataFile:
        s_line = line.replace("\n", "")
        
        total += len(s_line)
        res = getNumberOfCharacters(s_line)
        total_chars += res
        
    print("Result day 8 part 1: " + str(total - total_chars))
    
def number8_2():
    dataFile = open("data/day8.txt", "r")
    
    total_encoded = 0
    total_original = 0
    for line in dataFile:
        s_line = line.replace("\n", "")
        
        s_line_encoded = encode(s_line)
        
        total_encoded += len(s_line_encoded)
        total_original += len(s_line)
        
    print("Result day 8 part 2: " + str(total_encoded - total_original))
    
number8_1()        
number8_2()
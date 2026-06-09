AND = "AND"
OR = "OR"
LSHIFT = "LSHIFT"
RSHIFT = "RSHIFT"
NOT = "NOT"
MASK = 65535
NUM_BITS = 16

def bit_not(value, numbits=NUM_BITS):
    return (1 << numbits) - 1 - value
    
def getOperationValue(operation, value_1, value_2):
    # b_value_1 = bin(int(value_1))
    b_value_1 = int(value_1)
    if value_2:
        # b_value_2 = bin(int(value_2))
        b_value_2 = int(value_2)
    
    if operation == AND:
        aux = b_value_1 & b_value_2
    elif operation == OR:
        aux = b_value_1 | b_value_2
    elif operation == LSHIFT:
        aux = (b_value_1 << b_value_2) & MASK
    elif operation == RSHIFT:
        aux = b_value_1 >> b_value_2
    else:
        aux = bit_not(b_value_1)

    return str(aux)

def number7_1():    
    dataFile = open("data/day7.txt", "r")

    operations = []
    values = {}
    
    for line in dataFile:
        s_line = line.replace("\n", "")

        l_elements = s_line.split(" -> ")
        l_left = l_elements[0].split(" ")  
        l_right = l_elements[1]      
        if AND in s_line or OR in s_line or LSHIFT in s_line or RSHIFT in s_line: #two paremeters 
            value_1 = l_left[0]
            value_2 = l_left[2]
            operation = l_left[1]
            if value_1.isnumeric() and value_2.isnumeric():
                res = getOperationValue(operation, value_1, value_2)
                values[l_right] = res
            else:
                operations.append((value_1, operation, value_2, l_right))
        else: # NOT or direct assignation
            if NOT in s_line:
                value_1 = l_left[1]
                if value_1.isnumeric(): 
                    res = getOperationValue(NOT, value_1, None)
                    values[l_right] = res
                else:
                    operations.append((value_1, NOT, None, l_right))
            else:
                value_1 = l_left[0]
                if value_1.isnumeric():
                    values[l_right] = value_1
                else: #it is a wire
                    operations.append((value_1, None, None, l_right))

    while not "a" in values.keys():
        aux = []
        for value_1, operation, value_2, wire in operations:
            if operation:
                if value_1.isnumeric() and (not value_2 or value_2.isnumeric()):
                    res = getOperationValue(operation, value_1, value_2)
                    values[wire] = res
                else: # look for values
                    if value_1 in values.keys():
                        value_1 = values[value_1]
                    if value_2 in values.keys():
                        value_2 = values[value_2]
                    aux.append((value_1, operation, value_2, wire))
            else: 
                if value_1.isnumeric():
                    values[wire] = value_1
                else:
                    if value_1 in values.keys():
                        values[wire] = values[value_1]
                    else:
                        aux.append((value_1, operation, value_2, wire))
        operations = aux.copy()

    print("Result day 7 part 1: The a value is " + str(values["a"]))
    
def number7_2():    
    dataFile = open("data/day7_2.txt", "r")

    operations = []
    values = {}
    
    for line in dataFile:
        s_line = line.replace("\n", "")

        l_elements = s_line.split(" -> ")
        l_left = l_elements[0].split(" ")  
        l_right = l_elements[1]      
        if AND in s_line or OR in s_line or LSHIFT in s_line or RSHIFT in s_line: #two paremeters 
            value_1 = l_left[0]
            value_2 = l_left[2]
            operation = l_left[1]
            if value_1.isnumeric() and value_2.isnumeric():
                res = getOperationValue(operation, value_1, value_2)
                values[l_right] = res
            else:
                operations.append((value_1, operation, value_2, l_right))
        else: # NOT or direct assignation
            if NOT in s_line:
                value_1 = l_left[1]
                if value_1.isnumeric(): 
                    res = getOperationValue(NOT, value_1, None)
                    values[l_right] = res
                else:
                    operations.append((value_1, NOT, None, l_right))
            else:
                value_1 = l_left[0]
                if value_1.isnumeric():
                    values[l_right] = value_1
                else: #it is a wire
                    operations.append((value_1, None, None, l_right))

    while not "a" in values.keys():
        aux = []
        for value_1, operation, value_2, wire in operations:
            if operation:
                if value_1.isnumeric() and (not value_2 or value_2.isnumeric()):
                    res = getOperationValue(operation, value_1, value_2)
                    values[wire] = res
                else: # look for values
                    if value_1 in values.keys():
                        value_1 = values[value_1]
                    if value_2 in values.keys():
                        value_2 = values[value_2]
                    aux.append((value_1, operation, value_2, wire))
            else: 
                if value_1.isnumeric():
                    values[wire] = value_1
                else:
                    if value_1 in values.keys():
                        values[wire] = values[value_1]
                    else:
                        aux.append((value_1, operation, value_2, wire))
        operations = aux.copy()

    print("Result day 7 part 2: The a value is " + str(values["a"]))

number7_1()
number7_2()
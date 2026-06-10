def getNextPass(password):
    aux = list(password)
    
    for i in range(len(aux) - 1, -1, -1):
        if aux[i] < "z":
            aux[i] = chr(ord(aux[i]) + 1)
            break
        else:
            aux[i] = "a"
    
    return "".join(aux)

def passwordValid(password):

    if "i" in password or "o" in password or "l" in password:
        return False

    aux = list(password)

    current_pair = ""
    current_straigh = ""
    pairs = []
    straigh = False

    for i in range(0, len(aux)):
        if current_pair == "":
            current_pair = aux[i]
        else:
            if current_pair == aux[i]: # is a pair
                if not aux[i] in pairs: # is a new pair
                    pairs.append(aux[i])
                    current_pair = ""
            else:
                current_pair = aux[i] # the char can do a pair with the following
        
        if current_straigh == "":
            current_straigh = aux[i]
        elif len(current_straigh) == 1: 
            if ord(aux[i]) == ord(current_straigh) + 1: # next 
                current_straigh = current_straigh + aux[i]
            else: 
                current_straigh = aux[i] # straigh broken so, the current could start a new one
        else: # 2 chars
            if ord(aux[i]) == ord(current_straigh[-1]) + 1: # next 
                straigh = True
                current_straigh = ""
            else: 
                current_straigh = aux[i] # straigh broken so, the current could start a new one

    return len(pairs) >= 2 and straigh

def generatePass(password="cqjxjnds"):
    found = False

    while not found:
        password = getNextPass(password)
        if passwordValid(password):
            found = True
    
    return password 
   

def number11_1():
    password = generatePass()

    print("Result day 11 part 1: The new password id " + password)

def number11_2():
    password = generatePass("cqjxxyzz")
    
    print("Result day 11 part 2: The new password id " + password)

number11_1()
number11_2()
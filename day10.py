def lookAndSay(chain):
    i = 0
    aux = ""
    
    while i < len(chain):
        j = i + 1
        num = 1
        while j < len(chain):
            if chain[i] == chain[j]:
                num += 1
                j += 1
            else:
                break
        aux = aux + str(num) + chain[i]
        i += num 
                
    return aux

def number10_1():
    start = "1113122113"
    cicles = 40
    
    aux = start
    for i in range(0, cicles):
        aux = lookAndSay(aux)
        
    print("Result day 10 part 1: " + str(len(aux)))
    
def number10_2():
    start = "1113122113"
    cicles = 50
    
    aux = start
    for i in range(0, cicles):
        aux = lookAndSay(aux)
        
    print("Result day 10 part 2: " + str(len(aux)))
    
number10_1()
number10_2()
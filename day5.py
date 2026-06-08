import re

def hasEnoughVocals(chain):
    i_vocals = chain.count("a") + chain.count("e") + chain.count("i") + chain.count("o") + chain.count("u")
    
    return i_vocals >= 3

def hasLetterDuplicated(chain):
    l_chain = list(chain)
    
    for i in range(0, len(l_chain) - 1):
        if l_chain[i] == l_chain[i + 1]:
            return True
    
    return False

def hasGroupOfLetters(chain):
    search_list = ['ab', 'cd', 'pq', 'xy']
    
    for search_value in search_list:
        if search_value in chain:
            return True
        
    return False

def number5_1():
    dataFile = open("data/day5.txt", "r")
    
    nice_strings = 0
    for line in dataFile:
        s_line = line.replace("\n", "")
        
        if not hasEnoughVocals(s_line):
            continue
        if not hasLetterDuplicated(s_line):
            continue
        if hasGroupOfLetters(s_line):
            continue
        
        nice_strings += 1
        
    print("Result day 5 part 1: The number of nice strings is " + str(nice_strings))
    
# Test if a pair of letters appears at least two times without overlapping (aaa is overlap)
def hasPairOfLetters(chain):
    l_line = list(chain)
    
    for i in range(0, len(l_line) - 2):
        pair = "".join(l_line[i:i+2])
        if pair in "".join(l_line[i+2:]):
            return True
    
    return False

# Test if a letter is repeated but with one letter in the middle without any restriction about what letter is in the middle
def isLetterRepeated(chain):
    l_line = list(chain)
    
    for i in range(0, len(l_line) - 2):
        if l_line[i] == l_line[i+2]:
            return True
    
    return False
    
def number5_2():
    dataFile = open("data/day5.txt", "r")
    
    nice_strings = 0
    for line in dataFile:
        s_line = line.replace("\n", "")
        
        if not hasPairOfLetters(s_line):
            continue
        if not isLetterRepeated(s_line):
            continue
        
        nice_strings += 1
        
    print("Result day 5 part 2: The number of nice strings are " + str(nice_strings))
    
    
number5_1()
number5_2()
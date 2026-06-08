import re

def hasEnoughVocals(chain):
    i_vocals = chain.count("a") + chain.count("e") + chain.count("i") + chain.count("o") + chain.count("u")
    
    return i_vocals >= 3

def hasLetterDuplicated(chain):
    s_chain = list(chain)
    
    for i in range(0, len(s_chain) - 1):
        if s_chain[i] == s_chain[i + 1]:
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
    
    
number5_1()
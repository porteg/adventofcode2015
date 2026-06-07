import hashlib

def number4_1():
    md5_secret = "bgvyzdsv"

    i_index = 1
    res = ""

    while not res.startswith("00000"):
        md5_chain = md5_secret + str(i_index)
        md5_hash = hashlib.md5(md5_chain.encode())
        res = md5_hash.hexdigest()
        i_index += 1
    
    print("Result day 4 part 1: The first index with a MD5 that starts with 5 zeros is " + str(i_index - 1))

def number4_2():
    md5_secret = "bgvyzdsv"

    i_index = 1
    res = ""

    while not res.startswith("000000"):
        md5_chain = md5_secret + str(i_index)
        md5_hash = hashlib.md5(md5_chain.encode())
        res = md5_hash.hexdigest()
        i_index += 1
    
    print("Result day 4 part 2: The first index with a MD5 that starts with 5 zeros is " + str(i_index - 1))    

number4_1()
number4_2()
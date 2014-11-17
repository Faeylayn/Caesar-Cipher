import os
import sys
import string

def build_key1():
    test = string.lowercase
    g = []
    for x in test:
        g.append(x)
    return g

def build_key2():
    test = string.uppercase
    g = []
    for x in test:
        g.append(x)
    return g

def build_dict(key1, key2, shift):
    dic = {}
    for i in range(len(key1) - shift):
        dic[key1[i]] = key1[i + shift]
    for j in range(shift):
        dic[key1[len(key1) - shift + j]] = key1[j]
    for k in range(len(key2) - shift):
        dic[key2[k]] = key2[k + shift]
    for l in range(shift):
        dic[key2[len(key2) - shift + l]] = key2[l]

    return dic

def get_file():
    print "Please enter text file to be encrypted."
    f = raw_input()
    return f

def get_shift(key1):
    shift = 40
    while not (int(shift) < len(key1)):
        print "Please enter desired shift."
        shift = raw_input()
        
    
    return int(shift)
    
def apply_dict(dic, filename):
#    a = 0
#    text = []    
    with open('%s_encrypt.txt' % filename, 'w') as f:
           
        with open(filename, 'r') as o:
            for line in o:
#            text[a] = []
                for char in line:
                    if char in dic.keys():
                        f.write(dic[char])
                    else:
                        f.write(char)
    print "Encrypt done."

def main():
    key1 = build_key1()
    key2 = build_key2()

    shift = get_shift(key1)
    
    dic = build_dict(key1, key2, shift)

    getf = True

    while getf:
        filename = get_file()
        if not os.path.exists(filename):
            print "That file does not exist"
        else:
            getf = False
    
    apply_dict(dic, filename)


if __name__ == "__main__":

    main()


def build_key(case):
    test = string.%s % case
    g = []
    for x in test:
        g.append(x)
    return g

def build_dict(key1, key2, shift):
    dic = {}
    ciph1 = list(key1)
    ciph2 = list(key2)
    for i in range(len(key1) - shift):
        dic[key1[i]] = key1[i + shift]
    for j in range(shift):
        dic[key1[len(key1) - shift + j]] = key1[j]
    for k in range(len(key2) - shift):
        dic[key2[k]] = key2[k + shift]
    for l in range(shift):
        dic[key2[len(key2) - shift + l]] = key2[l]

    return dic


    

w1 = 'wrotek'
w2 = 'kotewr'
#w1 = 'kkttlls'
#w2 = 'ktttsll'


## ASCII Values O(n)
#def is_permutation(w1: str, w2:str) -> bool:
#    if len(w1) != len(w2): return False
#
#    sum1, sum2 = 0,0
#    for i in range(len(w1)):
#        sum1 += ord(w1[i])
#        sum2 += ord(w2[i])
#
#    if sum1 == sum2: return True
#    return False

## replace string -- stupid
#def is_permutation(w1: str, w2: str) -> bool:
#    if len(w1) != len(w2): return False
#
#    while len(w1)>0:
#        try:
#            w2.replace(w1[0], "", 1)
#            w1.replace(w1[0], "", 1)
#        except:
#            return False
#        print(w1)
#        print(w2)
#        if len(w1) != len(w2): return False
#    
#    return True


## Hash table O(n)?
#def is_permutation(w1: str, w2: str) -> bool:
#    if len(w1) != len(w2): return False
#
#    dict1= {}
#    dict2= {}
#
#    for i in range(len(w1)):
#        if w1[i] in dict1:
#            dict1[w1[i]] +=1
#        else:
#            dict1[w1[i]] = 0
#        if w2[i] in dict2:
#            dict2[w2[i]] +=1
#        else:
#            dict2[w2[i]] = 0
#
#    if dict1 == dict2:
#        return True
#    
#    return False

## Sorting
def is_permutation(w1: str, w2: str) -> bool:
    if len(w1) != len(w2): return False
    w1 = ''.join(sorted(w1))
    w2 = ''.join(sorted(w2))
    if w1 == w2:
        return True
    return False


if __name__ == '__main__':
    print(is_permutation(w1, w2))
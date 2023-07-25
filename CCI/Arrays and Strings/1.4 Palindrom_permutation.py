#w1 = "Tact Coa"
#w1 = "Maamda"


## Dictionary O(n+k)
#def have_permutation(w1: str) -> bool:
#    dict = {}
#    count =0
#    w1 = w1.casefold()
#    w1 = w1.split()
#    w1 = ''.join(w1)
#    if len (w1) ==0: return False
#
#    for i in range(len(w1)):
#        if w1[i] in dict:
#            dict[w1[i]] +=1
#        else:
#            dict[w1[i]] = 1
#    
#    for value in dict.values():
#        if value%2==1:
#            count +=1
#
#    if count >1: return False
#    return True


## Dictionary O(n)
def have_permutation(w1: str) -> bool:
    dict = {}
    count =0
    w1 = w1.casefold()
    w1 = w1.split()
    w1 = ''.join(w1)
    if len (w1) ==0: return False

    for i in range(len(w1)):
        if w1[i] in dict:
            dict[w1[i]] +=1
            count -=1
        else:
            dict[w1[i]] = 1
        
        if dict[w1[i]]%2==1:
            count +=1

    if count >1: return False
    return True

if __name__ == '__main__':
    print(have_permutation(w1))
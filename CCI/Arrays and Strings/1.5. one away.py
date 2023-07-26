w1 = "pale"
w2 = "ale"

def one_replace(w1: str, w2:str)-> bool:
    diff = False
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            if diff == True:
                return False
            diff = True
    return True

def one_change(w1: str, w2:str)-> bool:
    i, j = 0, 0
    while i < len(w1) and j < len(w2):
        if w1[i] != w2[j]:
            if i != j:
                return False
            i += 1
        else:
            j+=1
            i+=1
    return True

def one_away(w1: str, w2:str)-> bool:
    if abs(len(w1) - len(w2))>1 : return False

    if len(w1) - len(w2) == 0:
        return one_replace(w1, w2)
    
    if len(w1) - len(w2) == 1:
        return one_change(w1, w2)

    if len(w1) - len(w2) == -1:
        return one_change(w2, w1)

if __name__ == '__main__':
    print(one_away(w1,w2))

A = ['a','b','c','d','e','f']
P = [0,4,2,5,1,3]

def permutate(A: list, P: list)-> list:
    output =[]
    i =0
    if len(P) != len(A): return False

    while i<len(A):
        if i == P[i]:
            i+=1
            continue
        A[i],A[P[i]] = A[P[i]], A[i]
        P[P[i]], P[i] = P[i], P[P[i]]

        i+=1
    
    return A

if __name__ == "__main__":
    print(permutate(A,P))
#input = 'datastructure'
#input = 'AbcdeFghi'
#input = 'Aa'



## BRUTE FORCE O(n^2)
#def is_unique(input: str) -> bool:
#    if len(input) >0:
#        for i in range(len(input)):
#            for j in range(i+1,len(input)):
#                if input[i] == input[j]:
#                    return False
#        return True
#    return False


## Sorting Solution O(n(logn+1))
#def is_unique(input: str) -> bool:
#    if len(input)>0:
#        input = ''.join(sorted(input))
#        for i in range(len(input)-1):
#            if input[i] == input[i+1]:
#                return False
#        return True
#    return False


## Hash table
def is_unique(input: str) -> bool:
    hash = set()
    if len(input)>0:
        for i in range(len(input)):
            if input[i] in hash:
                return False
            hash.add(input[i])
        return True
    return False
    
    

if __name__ == '__main__':
    print(is_unique(input))
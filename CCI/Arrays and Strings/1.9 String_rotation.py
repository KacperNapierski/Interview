s1 = 'watawashw'
s2 = 'washwwata'
#
#s1 = 'waterbottle'
#s2 = 'erbottlewat'



### INDEX METHOD
##quick function simulation
#def is_Substring(i: int, s1: str, s2: str) ->bool:
#    s2 = s2[i:] + s2[:i]
#    if s2 == s1:
#        return True
#
#
#def is_string_rotated(s1: str, s2: str) ->bool:
#    
#    #conditions
#    if len(s1) !=len(s2): return False
#    if s1[0] == s2[0]:
#        if s1 == s2: return False
#    if s1 == "" or s2 == "": return False
#
#    #main program
#    for i in range(1, len(s1)):
#        if s2[i] == s1[0]:
#            if len(s2[i:]) == len(s1[:len(s1)-i]) and s2[i:] == s1[:len(s1)-i]:
#                print("check") # to see if sunction have more than one call
#                return is_Substring(i, s1, s2)
#    
#    return False

### SUBSTRING METHOD
def is_Substring(s1: str, s2: str) ->bool:
    x = s1.find(s2)
    if x >=0:
        return True
    
    else:
        return False

def is_string_rotated(s1: str, s2: str) ->bool:
    if len(s1) !=len(s2): return False
    if s1 == "" or s2 == "": return False

    s1s1 = s1+s1
    return is_Substring(s1s1, s2)


if __name__ == "__main__":
    print(is_string_rotated(s1, s2))
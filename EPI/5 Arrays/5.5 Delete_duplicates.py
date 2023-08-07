input = [2,3,5,5,7,11,11,11,13]
#

### HASHSET
#def delete_duplicates(input:list):
#    hash= set()
#    
#    for i in range(len(input)):
#        hash.add(input[i])
#    return hash

### IN PLACE
def delete_duplicates(input:list):
    current_val = input[0]
    i=1
    while i< len(input) - 1:
        if input[i]==current_val:
            input.pop(i)
            i-=1
        else:
            current_val = input[i]
        i +=1
    return input


if __name__ == "__main__":
    print(delete_duplicates(input))
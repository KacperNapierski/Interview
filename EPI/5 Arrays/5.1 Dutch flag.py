A = [0,1,2,3,0,4,5,7,2,1,1,4,9,8,3,2]
pivot_index = 3

### BRUTE FORCE
#def sorting(input: list, pivot_index: int) -> list:
#    length = len(A)
#    i = 0
#    pivot_value = A[pivot_index]
#    left_flag = False
#
#    while length > 0:
#
#        if A[i] > pivot_value:
#            A.append(A[i])
#            A.pop(i)
#        
#        elif A[i] < pivot_value and left_flag == True:
#            A.insert(0,A[i])
#            A.pop(i+1)
#            i+=1
#        
#        elif A[i] == pivot_value:
#            left_flag = True
#            i+=1
#
#        else:
#            i+=1
#        length -=1
#
#    return A


def sorting(input: list, pivot_index: int) -> list:
    ...


if __name__ == '__main__':
    print(sorting(A, pivot_index))
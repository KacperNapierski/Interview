#A = [0,1,2,3,0,4,5,7,2,1,1,4,9,8,3,2]
A = [0,1,2,0,2,1,1]
pivot_index = 1

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

### TWO POINTS - slow
#def sorting(input: list, pivot_index: int) -> list:
#    pivot_value = A[pivot_index]
#
#    for i in range(len(A)):
#        for j in range(i+1, len(A)):
#            print(f"i= {i}")
#            print(f"j= {j}")
#            print(f"A = {A}")
#            if A[j] < pivot_value:
#                A[i],A[j] = A[j], A[i]
#                break
#    for i in reversed(range(len(A))):
#        for j in reversed(range(i)):
#            print("reversed")
#            print(f"i= {i}")
#            print(f"j= {j}")
#            print(f"A = {A}")
#            if A[j] > pivot_value:
#                A[i],A[j] = A[j], A[i]
#                break
#    
#    return A


def sorting(input: list, pivot_index: int) -> list:
    pivot_value = A[pivot_index]
    smaller =0
    larger = len(A)-1

    for i in range(len(A)):
        print(f"i= {i}")
        print(f"smaller= {smaller}")
        print(f"A = {A}")
        if A[i] < pivot_value:
            A[i], A[smaller] = A[smaller], A[i]
            smaller +=1
    for i in reversed(range(len(A))):
        print(f"i= {i}")
        print(f"larger= {larger}")
        print(f"A = {A}")
        if A[i] > pivot_value:
            A[i], A[larger] = A[larger], A[i]
            larger -=1
    return A

if __name__ == '__main__':
    print(sorting(A, pivot_index))
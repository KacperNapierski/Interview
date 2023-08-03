A = [1,2,9]

def increment(input: list) -> list:
    for i in reversed(range(len(A))):
        if A[i]==9:
            A[i]=0
            print(i)
            if i == 0:
                A.insert(0,1)

        else:
            A[i] +=1
            break
        
    return A
        

if __name__ == '__main__':
    print(increment(A))
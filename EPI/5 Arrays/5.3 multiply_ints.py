A = [1,6,8]
B = [9,8]

def multiply(A: list, B:list)-> list:
    if A[0] < 0 ^ B[0] < 0:
        sign = -1
    else:
        sign = 1
    
    result = [0] * (len(A) + len(B))
    print(result)
    print("----------")
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            result[i+j+1] += A[i]*B[j]
            print(result)
            result[i+j] += result[i+j+1]//10
            print(result)
            result[i+j+1] %= 10
            print(result)
            print("----------")
    
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    print(result)

    return [sign* result[0]+ result[1:]]
if __name__ == "__main__":
    print(multiply(A,B))
A = [3,3,1,0,2,0,1]
#A = [4,2,0,0,1,1,0]

def advance_array(input:list) -> bool:
    print("start")
    highest_travel, index, i = 0, 0, 0
    while i<len(input)-1:
        for j in range(i+1,input[i]+i+1):
            print(f"i={i}, j={j},A[j]={A[j]}")
            if j == len(input) - 1: return True
            if input[j] == 0: continue
            if j + input[j] > highest_travel:
                if input[input[j]+j] != 0:
                    highest_travel = input[j] + j
                    index = j
                elif input[input[j]+j] == 0 and input[j]+j == len(input)-1:
                    return True
                else:
                    continue

        i = index
    return False

if __name__ == "__main__":
    print(advance_array(A))
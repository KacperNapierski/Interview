matrix = [[1,9,7,6,6],
          [3,5,4,0,1],
          [2,1,8,4,3],
          [0,7,2,9,8]]

N = len(matrix)
M = len(matrix[0])

def find_zeros(matrix)-> list: #O(M*N)
    zeros = []
    for m in range(M):
        for n in range(N):
            if matrix[n][m] == 0:
                zeros.append([n,m])
    print(zeros)
    return zeros

def zero_matrix(zeros, matrix)-> list: #O(zeros*(M+N))
    for position in zeros:
        for m in range(M):
            print(position)
            print(position[0])
            if matrix[position[0]][m] == 0:
                continue
            matrix[position[0]][m] = 0
        
        for n in range(N):
            if matrix[n][position[1]] == 0:
                continue
            matrix[n][position[1]] = 0

    
    return matrix


if __name__ == '__main__': #O(M*N + zeros*(M+N))
    zeros = find_zeros(matrix)
    print(zero_matrix(zeros, matrix))
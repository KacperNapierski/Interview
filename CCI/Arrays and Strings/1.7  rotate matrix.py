matrix = [[1,8,7,4,5,1],
          [6,9,2,3,6,1],
          [7,11,10,2,5,1],
          [14,8,9,2,4,1],
          [3,12,5,1,7,1],
          [1,1,1,1,1,1]]


def rotate_matrix(matrix):
    N = len(matrix) #N=5

    for j in range(int(N/2)): #j=(0,1)
        print(j)
        for i in range(j, N-1-j): #i=(0,4), i= (1,3)
            print(i)
            matrix[j][i], matrix[i][N-1-j], matrix[N-1-j][N-1-i], matrix[N-1-i][j] = matrix[i][N-1-j], matrix[N-1-j][N-1-i], matrix[N-1-i][j], matrix[j][i]
    return matrix


if __name__ == '__main__':
    print(rotate_matrix(matrix))

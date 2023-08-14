#A = [3,5,7,2,10]
A = [1,7,9,8,5,4,10,6,2,3]
A.sort()

for i in range(2, len(A),2):
    A[i-1], A[i] = A[i], A[i-1]

print(A)
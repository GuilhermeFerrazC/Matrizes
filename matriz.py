A = [[3, 1, 3],
     [6, 5, 5]]

B = [[100, 50],
     [50, 100],
     [50, 50]]

# Multiplicação
def multiply_matrices(A, B):
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
                
    return result

C = multiply_matrices(A, B)
if isinstance(C, str):
    print(C)
else:
    for row in C:
        print(row)
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions incompatible for multiplication")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def matrix_add(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have same dimensions for addition")

    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_subtract(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have same dimensions for subtraction")

    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def matrix_power(A, n):
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be square for power operation")
    if n == 0:
        return [[1 if i == j else 0 for j in range(len(A))] for i in range(len(A))]

    if n == 1:
        return A

    if n % 2 == 0:
        half = matrix_power(A, n // 2)
        return matrix_multiply(half, half)
    else:
        return matrix_multiply(A, matrix_power(A, n - 1))


def is_symmetric(A):
    if len(A) != len(A[0]):
        return False
    return all(A[i][j] == A[j][i] for i in range(len(A)) for j in range(len(A)))


def determinant(A):
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be square")

    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    det = 0
    for j in range(n):
        minor = [[A[i][k] for k in range(n) if k != j] for i in range(1, n)]
        det += ((-1) ** j) * A[0][j] * determinant(minor)
    return det

def rotate_matrix(A):
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be square to rotate")

    n = len(A)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            top = A[first][i]
            A[first][i] = A[last - offset][first]
            A[last - offset][first] = A[last][last - offset]
            A[last][last - offset] = A[i][last]
            A[i][last] = top
    return A
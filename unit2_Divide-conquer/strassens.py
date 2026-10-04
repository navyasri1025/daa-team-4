
def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def subtract_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def strassen(A, B):
    n = len(A)

    # Base case: multiply 1x1 matrices
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Divide matrix A into four quadrants
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    # Divide matrix B into four quadrants
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Calculate seven products
    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, subtract_matrix(B12, B22))
    M4 = strassen(A22, subtract_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(subtract_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(subtract_matrix(A12, A22), add_matrix(B21, B22))

    # Combine the four result quadrants
    C11 = add_matrix(subtract_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(add_matrix(subtract_matrix(M1, M2), M3), M6)

    # Join the quadrants
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])

    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


def main():
    n = int(input("Enter matrix order (power of 2): "))

    if n <= 0 or (n & (n - 1)) != 0:
        print("Error: Matrix order must be a positive power of 2.")
        return

    print("Enter elements of Matrix A:")
    A = [list(map(int, input().split())) for _ in range(n)]

    print("Enter elements of Matrix B:")
    B = [list(map(int, input().split())) for _ in range(n)]

    result = strassen(A, B)

    print("\nResultant Matrix (A x B):")
    for row in result:
        print(*row)

    print("\nTime Complexity: O(n^log2(7)) ≈ O(n^2.807)")


if __name__ == "__main__":
    main()
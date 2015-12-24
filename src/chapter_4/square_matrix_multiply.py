def square_matrix_multiply(a, b):
    n = len(a)
    c = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            c_ij = 0

            for k in range(n):
                c_ij += a[i][k] * b[k][j]

            c[i][j] = c_ij

    return c

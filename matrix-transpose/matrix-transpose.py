import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows = len(A)
    cols = len(A[0])
    M = np.zeros((cols, rows))

    for i in range(cols):
        for j in range(rows):
            M[i][j] = A[j][i]

    return M
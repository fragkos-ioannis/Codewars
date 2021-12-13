# Without the use of numpy's dot function  

import numpy as np

def matrix_mult(a, b):
    result = np.zeros((len(a), len(b[0])), dtype=int)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result.tolist()

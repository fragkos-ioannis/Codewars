import numpy as np

def get_matrix(n):
    if n == 0:
        return []
    else:
        zerom = np.zeros(((n, n)), dtype = int)
        for i in range(n):
            for j in range(n):
                if i == j:
                    zerom[i][j] += 1
        return zerom.tolist()

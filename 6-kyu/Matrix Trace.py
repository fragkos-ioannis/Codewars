def trace(matrix):
    sum = 0
    if not matrix or len(matrix) != len(matrix[0]):
        return None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum += matrix[i][j]
    return sum
                

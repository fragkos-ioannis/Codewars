def check(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "k":
                king_row = i
                king_col = j
            if board[i][j] == "q":
                queen_row = i
                queen_col = j
    diagonal_row = abs(king_row - queen_row)
    diagonal_col = abs(king_col - queen_col)
    
    if king_row == queen_row or king_col == queen_col:
        return True
    
    return True if diagonal_row == diagonal_col else False
    

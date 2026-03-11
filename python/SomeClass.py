def findRows(board):
    updated_board = []
    for row in range(9):
        current_row = [board[row][x] for x in range(9)]
        updated_board.append(current_row)
    return updated_board


def findCols(board):
    updated_board = []
    for x in range(9):
        current_col = [board[row][x] for row in range(9)]
        updated_board.append(current_col)
    return updated_board


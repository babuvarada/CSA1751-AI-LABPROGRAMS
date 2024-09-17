
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_nqueens(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nqueens(board, col + 1):
                return True
            board[i][col] = 0
    return False
def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
def main():
    N = 8
    board = [[0 for _ in range(N)] for _ in range(N)]
    if solve_nqueens(board, 0):
        print_board(board)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()

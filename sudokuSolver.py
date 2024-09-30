#All the comments are for the items above it
def isValid(board, row, col, num):
    # Check if the number is in the current row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Function to check if placing a number is valid

    for i in range(9):
        if board[i][col] == num:
            return False
    # Checking if the number is in the current column


    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(startRow, startRow + 3):
        for j in range(startCol, startCol + 3):
            if board[i][j] == num:
                return False
    # Checking if the number is in the current 3x3 subgrid

    return True


def solveSudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if isValid(board, row, col, num):
                        board[row][col] = num  # Placing the number

                        if solveSudoku(board):  # Recursively trying to solve the rest
                            return True

                        board[row][col] = 0  # Backtracking if needed

                return False  # If no number is valid, then we backtrack
    return True
# Function to solve the Sudoku puzzle using backtracking
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
# Function to print the Sudoku board

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
# Example Sudoku board (0 represents empty cells)

if solveSudoku(board):
    print("Solved Sudoku:")
    print_board(board)
else:
    print("No solution exists")

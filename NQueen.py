# Function to check if a queen can be placed on the board at position (row, col)
def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

# Function to solve the n-Queen problem using backtracking
def solve_n_queen(board, row, n):
    # Base case: If all queens are placed, return True
    if row == n:
        return True
    
    # Try placing a queen in all columns one by one
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row] = col
            
            # Recursively place queens in the next row
            if solve_n_queen(board, row + 1, n):
                return True
            
            # Backtrack: Remove the queen (if placing the queen leads to no solution)
            board[row] = -1
    
    # If no valid position is found, return False
    return False

# Function to print the chessboard
def print_board(board, n):
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(' '.join(row))
    print()

# Main function to solve the n-Queen problem
def n_queen(n):
    # Initialize the board with -1 (no queens placed yet)
    board = [-1] * n
    
    if solve_n_queen(board, 0, n):
        print_board(board, n)
    else:
        print(f"No solution exists for {n} queens.")

# Example usage
n = 8  # Change n to test different sizes
n_queen(n)

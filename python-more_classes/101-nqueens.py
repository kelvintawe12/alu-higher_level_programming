#!/usr/bin/python3
import sys


def print_usage():
    """Prints the usage message"""
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """Solve the N queens problem and print all solutions"""
    def solve(board, row):
        if row == N:
            print([[i, board[i]] for i in range(N)])
        else:
            for col in range(N):
                if is_valid(board, row, col):
                    board[row] = col
                    solve(board, row + 1)
                    board[row] = -1

    board = [-1] * N
    solve(board, 0)
def main():
    if len(sys.argv) != 2:
        print_usage()
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(N)

if __name__ == "__main__":
    main()

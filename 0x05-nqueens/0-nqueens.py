#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """function that prints usage message and exits"""
    print("Usage: nqueens N")
    sys.exit(1)


def print_invalid_number_and_exit():
    """Function that prints message if N is not a number"""
    print("N must be a number")
    sys.exit(1)


def print_small_number_and_exit():
    """Function that prints message if N is a small number"""
    print("N must be at least 4")
    sys.exit(1)


def solve_nqueens(n):
    """Function that solves the n queens problem"""
    def is_not_under_attack(board, row, col):
        """Check if placing a queen at (row, col) is safe"""
        for prev_row in range(row):
            # Check colum and diagnols for conflicts
            if (board[prev_row] == col or
                    board[prev_row] - prev_row == col - row or
                    board[prev_row] + prev_row == col + row):
                return False
            return True

    def solve(row):
        """Recursive function to place queens on the board"""
        if row == n:
            # if all queens are placed, add the solution
            solutions.append([[a, board[a]] for a in range(n)])
            return
        for col in range(n):
            if is_not_under_attack(board, row, col):
                # Place queen
                board[row] = col
                # Move to next row
                solve(row + 1)
    solutions = []
    # Initialize the board
    board = [-1] * n
    # Start solving from the first row
    solve(0)
    return solutions


def main():
    """main"""
    if len(sys.argv) != 2:
        print_usage_and_exit()
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_invalid_number_and_exit()
    if n < 4:
        print_small_number_and_exit()
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

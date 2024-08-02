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


def is_not_under_attack(board, row, col):
    """Check if placing a queen at (row, col) is safe"""
    for i in range(row):
        # Check colum and diagnols for conflicts
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def solve_nqueens(n, row, board, result):
    """Function that solves the n queen problem"""
    if row == n:
        # if all queens are placed, add the solution
        result.append(board[:])
        return
    for col in range(n):
        if is_not_under_attack(board, row, col):
            # Place queen
            board[row] = col
            # Move to next row
            solve_nqueens(n, row + 1, board, result)


def print_board(board):
    """Function that prints the board"""
    print("[", end="")
    for i, col in enumerate(board):
        if i > 0:
            print(", ", end="")
        print(f"[{i}, {col}]", end="")
    print("]")


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
    result = []
    solve_nqueens(n, 0, [-1] * n, result)
    for board in result:
        print_board(board)


if __name__ == "__main__":
    main()

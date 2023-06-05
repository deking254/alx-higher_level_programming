#!/usr/bin/python3
"""
    a function for
    placing N non-attacking
    queens on an N×N chessboard
"""
import sys


def n_queens(n):
    def is_safe(board, row, col):
        """function to check for the suitability of the combinations"""
        for i in range(row):
            if board[i] == col or board[i] - i == col - row:
                return False
            if board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        """solve is the function to create the number combinations"""
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
    result = []
    board = [-1] * n
    solve(board, 0)
    return result


def print_solutions(solutions):
    """the function to convert the numbers to pairs"""
    for solution in solutions:
        pairs = []
        for row, col in enumerate(solution):
            pairs.append([row, col])
        print(pairs)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    else:
        try:
            n = int(sys.argv[1])
            if n < 4:
                print("N must be at least 4")
                exit(1)
            else:
                print_solutions(n_queens(n))
        except Exception:
            print("N must be a number")
            exit(1)

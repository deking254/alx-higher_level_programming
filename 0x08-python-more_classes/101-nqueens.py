#!/usr/bin/python3
"""
    a function for
    placing N non-attacking
    queens on an N×N chessboard
"""
import sys


def n_queens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i] == col:
                return False
            # Check if there is a queen in the same diagonal
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(board, row):
        if row == n:
            # All queens have been placed
            result.append(board.copy())
            return

        for col in range(n):
            if is_safe(board, row, col):
                # Place the queen and move to the next row
                board[row] = col
                solve(board, row + 1)
                # Backtrack and try the next column
                board[row] = -1

    result = []
    board = [-1] * n
    solve(board, 0)
    print(result)
    return result


if __name__ == '__main__':
    n_queens(int(sys.argv[1]))

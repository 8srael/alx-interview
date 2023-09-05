#!/usr/bin/python3

"""N queens problem"""

import sys


def solveNQueens(n):
    """return all possible solutions
    to the N queens problem
    """
    col = set()
    posDiag = set()
    negDiag = set()
    res = []
    board = [['.'] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append([[r, c] for r in range(n) for c in range(n)
                        if board[r][c] == 'Q'])
            return
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = 'Q'
            backtrack(r + 1)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = '.'
    backtrack(0)
    return res


def get_input():
    """ Validate program args

        Returns:
            int: the size of the chessboard
    """

    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


n = get_input()
solutions = solveNQueens(n)
for case in solutions:
    print(case)

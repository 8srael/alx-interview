#!/usr/bin/python3

"""N queens problem"""

from typing import List
import sys


def solveNQueens(n: int) -> List[List[str]]:
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    solutions = solveNQueens(int(sys.argv[1]))
    for case in solutions:
        print(case)

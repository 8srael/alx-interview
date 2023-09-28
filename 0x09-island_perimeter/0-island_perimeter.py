#!/usr/bin/python3

""" Task 0. Island Perimeter """


def island_perimeter(grid):
    """
        Returns the perimeter of the island described in grid
    """
    visited = set()
    row = len(grid)
    col = len(grid[0])

    def dfs(i, j):
        if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0

        visited.add((i, j))
        return dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)

    for i in range(row):
        for j in range(col):
            if(grid[i][j] == 1):
                return dfs(i, j)

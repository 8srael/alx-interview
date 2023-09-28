#!/usr/bin/python3

""" Task 0. Island Perimeter """


def island_perimeter(grid):
    """
        Returns the perimeter of the island described in grid
    """

    visited = set()
    row = len(grid)
    col = len(grid[0])
    perimeter = 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
            return 1

        if (i, j) in visited:
            return 0

        visited.add((i, j))
        perimeter = dfs(i + 1, j)
        perimeter += dfs(i, j + 1)
        perimeter += dfs(i - 1, j)
        perimeter += dfs(i, j - 1)
        return perimeter

    for i in range(row):
        for j in range(col):
            if(grid[i][j] == 1):
                return dfs(i, j)

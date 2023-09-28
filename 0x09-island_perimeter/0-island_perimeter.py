#!/usr/bin/python3

""" Task 0. Island Perimeter """


def island_perimeter(grid):
    """
        Returns the perimeter of the island described in grid
    """
    row = len(grid)
    col = len(grid[0])

    visited = [[0 for x in range(col)] for y in range(row)]

    def dfs(i, j):
        """Depth first search method"""
        if i < 0 or i > row-1 or j < 0 or j > col-1 or grid[i][j] == 0:
            return 1

        if visited[i][j]:
            return 0
        visited[i][j] = 1

        return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j+1) + dfs(i, j-1)

    for x in range(row):
        for y in range(col):
            if grid[x][y] == 1:
                return dfs(x, y)

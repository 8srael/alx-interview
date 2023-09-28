#!/usr/bin/python3

""" Task 0. Island Perimeter """


def dfs(grid, i, j, visited):
    """ Depth First Search"""
    row = len(grid)
    col = len(grid[0])

    if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
        return 1

    if (i, j) in visited:
        return 0

    visited.add((i, j))
<<<<<<< HEAD
    return dfs(grid, i + 1, j, visited) + \
         dfs(grid, i, j + 1, visited) + \
         dfs(grid, i - 1, j, visited) + \
         dfs(grid, i, j - 1, visited)
=======
    return (
        dfs(grid, i + 1, j, visited) +
        dfs(grid, i, j + 1, visited) +
        dfs(grid, i - 1, j, visited) +
        dfs(grid, i, j - 1, visited)
    )
>>>>>>> fed2b7a73518702b475fce0eb251b217523d66de


def island_perimeter(grid):
    """
        Returns the perimeter of the island described in grid
    """
    visited = set()
    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        for j in range(col):
            if(grid[i][j] == 1):
                return dfs(grid, i, j, visited)

## 0x09. Island Perimeter

This project contains interview coding challenges.

## Tasks To Complete

+ [x] 0. **Island Perimeter**<br/>[0-island_perimeter.py](0-island_perimeter.py) contains a module with a function that returns the perimeter of the island perimeter described in a grid, with the following requirements:
  + Prototype: `def island_perimeter(grid)`.
  + Return: perimeter of the island described in `grid`.
  + `grid` is a list of list of integers:
    + `0` represents a water zone.
    + `1` represents a land zone.
    + One cell is a square with side length `1`.
    + Grid cells are connected horizontally/vertically (not diagonally).
    + Grid is rectangular, with its width and height not exceeding `100`.
  + The grid is completely surrounded by water
  + There is only one island (or nothing).
  + The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
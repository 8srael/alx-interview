#!/usr/bin/python3

""" Rotate 2D Matrix module """


def transpose(matrix):
    """ transpose n * n matrix """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverseRow(matrix):
    """ Reverse matrice rows """
    i = j = row = 0
    n = len(matrix)
    while row < n:
        i = 0
        j = n - 1
        while i < j:
            matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]
            i += 1
            j -= 1
        row += 1


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise. """
    transpose(matrix)
    reverseRow(matrix)

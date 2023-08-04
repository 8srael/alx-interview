#!/usr/bin/python3
"""
    A module for working with lockboxes.
"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    pile = [0]

    while pile:
        actualBox = pile.pop()
        for key in boxes[actualBox]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                pile.append(key)
    return all(visited)

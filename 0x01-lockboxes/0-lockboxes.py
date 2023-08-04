#!/usr/bin/python3
"""
    A module for working with lockboxes.
"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""
    def exploreBox(boxIndex, visited):
        """Explore a box and mark all the boxes that can be opened"""
        if visited[boxIndex]:
            return
        visited[boxIndex] = True

        for key in boxes[boxIndex]:
            if 0 <= key < len(boxes):
                exploreBox(key, visited)

    n = len(boxes)
    visited = [False] * n
    exploreBox(0, visited)

    return all(visited)

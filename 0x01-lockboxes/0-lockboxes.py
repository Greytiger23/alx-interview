#!/usr/bin/python3
"""Method that determines if all boxes can be opened"""


def canUnlockAll(boxes):
    """function to show results"""
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    stack = [0]

    while stack:
        present_box = stack.pop()

        for key in boxes[present_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    return all(unlocked)

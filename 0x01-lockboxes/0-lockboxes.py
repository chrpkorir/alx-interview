#!/usr/bin/python3

def canUnlockAll(boxes):
    """Unlock array of boxes of keys with indices. """
    index = 0
    check = {}
    size = len(boxes)

    for keys in boxes:
        if len(keys) == 0 or index == 0:
            check[index] = -1  # box is empty
        for key in keys:
            if key < size and key != index:
                check[key] = key
        if len(check) == size:
            return True
        index += 1
    return False

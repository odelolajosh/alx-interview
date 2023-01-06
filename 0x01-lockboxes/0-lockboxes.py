#!/usr/bin/python3
""" This module contains `canUnlockAll` function """


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened suppose
    each boxes, numbered sequentially from 0 to n-1, contain
    keys to other boxes.
    """
    unlocked_boxes = set([0])  # boxes[0] is the initially given key
    keys = set(boxes[0]).difference(unlocked_boxes)

    while len(keys) > 0:
        box_id = keys.pop()
        if not box_id or box_id < 0 or box_id >= len(boxes):
            continue
        if box_id not in unlocked_boxes:
            keys = keys.union(boxes[box_id])
        unlocked_boxes.add(box_id)
    return len(boxes) == len(unlocked_boxes)

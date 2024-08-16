#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.
"""


from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all boxes can be unlocked.

    Args:
    boxes (List[List[int]]): A list of lists
    where each sublist represents the keys in a box.

    Returns:
    bool: True if all boxes can be unlocked, otherwise False.
    """
    queue = [0]
    unlocked_boxes = set([0])

    # Process the queue
    while queue:
        current_box = queue.pop(0)
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.add(key)
                queue.append(key)

    return len(unlocked_boxes) == len(boxes)

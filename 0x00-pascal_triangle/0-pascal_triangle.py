#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []


    """ initializing an empty resulting array """
    pascal = [[] for idx in range(n)]

    for li in range(n):
        for col in range(li+1):
            if col == 0 or col == li:
                pascal[li].append(1)
            else:
                pascal[li].append(pascal[li - 1][col - 1] + pascal[li - 1][col])
                return pascal

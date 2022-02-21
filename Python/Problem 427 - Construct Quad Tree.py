"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        row_sum = sum([sum(i) for i in grid])
        if(row_sum == pow(len(grid),2)):
            return Node(True, True, None, None, None, None)
        elif row_sum == 0:
            return Node(False, True, None, None, None, None)
        else:
            N = len(grid)
            half = N//2
            top_left = [grid[i][:half] for i in range(half)]
            top_right = [grid[i][half:] for i in range(half)]
            bottom_left = [grid[i][:half] for i in range(half, N)]
            bottom_right = [grid[i][half:] for i in range(half, N)]
            node = Node(True, False, self.construct(top_left), self.construct(top_right), self.construct(bottom_left), self.construct(bottom_right))
            return node
        
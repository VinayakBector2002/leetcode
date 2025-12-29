# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Given the root of a binary tree with **unique values** and the values of **two different nodes** of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

BFS -> Marking each level in a dict -> Nodes.val: (Level, parent)

Questions:
Are they guarantee to exist?
'''
from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        q = deque()
        q.append(root)
        nMap = {root.val : (0, None)}
        
        def bfs():
            while q:
                for _ in range(len(q)):
                    current = q.popleft()
                    
                    if current.left:
                        nMap[current.left.val] = (nMap[current.val][0] + 1, current.val)
                        q.append(current.left)
                        
                    if current.right:
                        nMap[current.right.val] = (nMap[current.val][0] + 1, current.val)
                        q.append(current.right)
        bfs()
        
        if x in nMap and y in nMap:
            xVal, yVal = nMap[x], nMap[y]
            return True if xVal[0] == yVal[0] and xVal[1] != yVal[1] else False
        
        return False